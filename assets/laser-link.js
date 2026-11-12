// Small MQTT-over-WebSocket link between the phone remote and the deck, on the private channel.
// It carries the laser pointer and, first choice, the remote's commands and the deck's replies.
// A socket that goes quiet (a phone that slept, a network that changed) is closed and reopened.
(() => {
  const BROKERS = ['wss://broker.hivemq.com:8884/mqtt', 'wss://broker.emqx.io:8084/mqtt'];
  const enc = new TextEncoder(), dec = new TextDecoder();
  const str = s => { const b = enc.encode(s); return [b.length >> 8, b.length & 255, ...b]; };
  const size = n => { const o = []; do { let d = n % 128; n = Math.floor(n / 128); if (n) d |= 128; o.push(d); } while (n); return o; };
  const packet = (type, body) => new Uint8Array([type, ...size(body.length), ...body]);

  function open(url, topic, listen, onOpen, onClose) {
    const ws = new WebSocket(url, 'mqtt');
    ws.binaryType = 'arraybuffer';
    let ping, dog, heard = Date.now(), up = false;
    const giveUp = setTimeout(() => { if (!up) ws.close(); }, 8000);        // a broker that never answers
    dog = setInterval(() => { if (Date.now() - heard > 40000) ws.close(); }, 5000);
    ws.kick = () => {                                                       // after sleep: prove the socket still works
      if (ws.readyState !== 1) return;
      const asked = Date.now();
      try { ws.send(new Uint8Array([0xC0, 0])); } catch { return ws.close(); }
      setTimeout(() => { if (heard < asked) ws.close(); }, 3500);
    };
    ws.onopen = () => {
      const id = 'cqts' + Math.random().toString(36).slice(2, 12);
      ws.send(packet(0x10, [...str('MQTT'), 4, 2, 0, 60, ...str(id)]));
    };
    ws.onmessage = e => {
      const d = new Uint8Array(e.data);
      heard = Date.now();
      for (let i = 0; i < d.length;) {
        const type = d[i] >> 4; let j = i + 1, len = 0, m = 1, b;
        do { b = d[j++]; len += (b & 127) * m; m *= 128; } while (b & 128);
        if (type === 2) {                                // connected
          if (d[j + 1] !== 0) { ws.close(); return; }
          up = true; clearTimeout(giveUp);
          if (listen) ws.send(packet(0x82, [0, 1, ...str(topic), 0]));
          ping = setInterval(() => ws.readyState === 1 && ws.send(new Uint8Array([0xC0, 0])), 15000);
          onOpen(ws);
        } else if (type === 3 && listen) {               // message
          const n = (d[j] << 8) | d[j + 1];
          listen(dec.decode(d.subarray(j + 2 + n, j + len)));
        }
        i = j + len;
      }
    };
    let done = false;
    ws.onclose = () => { if (done) return; done = true; clearInterval(ping); clearInterval(dog); clearTimeout(giveUp); onClose(); };
    ws.onerror = () => {};
    return ws;
  }

  // Listener: stays on every broker, so it hears a sender on whichever one that sender could reach.
  // onState(up) reports whether at least one broker is listening.
  window.laserListen = (topic, onMessage, onState) => {
    let stopped = false; const socks = new Map(), live = new Set();
    const tell = () => onState?.(live.size > 0);
    const start = url => {
      if (stopped) return;
      socks.set(url, open(url, topic, onMessage, () => { live.add(url); tell(); },
        () => { live.delete(url); tell(); setTimeout(() => start(url), 2000); }));
    };
    BROKERS.forEach(start);
    return {
      close() { stopped = true; socks.forEach(s => s.close()); },
      kick() { socks.forEach(s => s.kick?.()); },
      get up() { return live.size > 0; }
    };
  };

  // Sender: keeps a link to every broker and sends on each one that is open, so a message arrives
  // even if the listener could reach only one of them. Receivers ignore the copies.
  window.laserSend = (topic, onState) => {
    let stopped = false; const socks = new Map(), live = new Map();
    const tell = () => onState(live.size > 0);
    const start = url => {
      if (stopped) return;
      socks.set(url, open(url, topic, null, ws => { live.set(url, ws); tell(); },
        () => { live.delete(url); tell(); setTimeout(() => start(url), 2000); }));
    };
    BROKERS.forEach(start);
    return {
      send(text) {
        let sent = false;
        live.forEach(ws => { if (ws.readyState === 1) { ws.send(packet(0x30, [...str(topic), ...enc.encode(text)])); sent = true; } });
        return sent;
      },
      close() { stopped = true; socks.forEach(s => s.close()); },
      kick() { socks.forEach(s => s.kick?.()); },
      get up() { return live.size > 0; }
    };
  };
})();
