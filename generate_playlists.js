const https = require('https');

const INSTANCES = [
  'https://invidious.jing.rocks',
  'https://vid.puffyan.us',
  'https://invidious.nerdvpn.de'
];

const PLAYLISTS = [
  { id: 'pl_sertanejo', name: 'Top Sertanejo 2024', description: 'As mais tocadas do sertanejo', search: 'top sertanejo 2024 oficial' },
  { id: 'pl_funk', name: 'Funk Hits', description: 'Os maiores hits do funk brasileiro', search: 'melhores funk 2024' },
  { id: 'pl_forro', name: 'Paredão Forró', description: 'Só as melhores do forró e piseiro', search: 'top forró piseiro 2024' },
  { id: 'pl_pop', name: 'Pop Internacional', description: 'Hits do pop mundial', search: 'top hits pop 2024' },
  { id: 'pl_lofi', name: 'Lo-Fi Chill', description: 'Para relaxar e focar', search: 'lofi hip hop radio beats to relax study to' },
  { id: 'pl_reggaeton', name: 'Reggaeton Caliente', description: 'As melhores do reggaeton', search: 'top reggaeton 2024' },
  { id: 'pl_hiphop', name: 'Hip-Hop / Rap', description: 'Batidas pesadas e rimas afiadas', search: 'top rap hip hop 2024' }
];

async function fetchSearch(query) {
  for (let inst of INSTANCES) {
    try {
      return await new Promise((resolve, reject) => {
        const req = https.get(`${inst}/api/v1/search?q=${encodeURIComponent(query)}&type=video`, { timeout: 10000 }, (res) => {
          let data = '';
          res.on('data', chunk => data += chunk);
          res.on('end', () => {
            if (res.statusCode === 200) {
              resolve(JSON.parse(data));
            } else {
              reject(new Error(`Status ${res.statusCode}`));
            }
          });
        });
        req.on('error', reject);
        req.on('timeout', () => { req.destroy(); reject(new Error('Timeout')); });
      });
    } catch (e) {
      // try next
    }
  }
  return [];
}

async function run() {
  const finalPlaylists = [];
  for (let p of PLAYLISTS) {
    console.log(`Buscando ${p.name}...`);
    const results = await fetchSearch(p.search);
    const tracks = [];
    for (let i = 0; i < Math.min(10, results.length); i++) {
      const v = results[i];
      if (!v) continue;
      const hqThumb = v.videoThumbnails ? v.videoThumbnails.find(t => t.quality === 'mqdefault' || t.quality === 'high') : null;
      const thumbUrl = hqThumb ? hqThumb.url : `https://i.ytimg.com/vi/${v.videoId}/mqdefault.jpg`;
      
      tracks.push({
        videoId: v.videoId,
        title: v.title,
        uploader: v.author,
        durationText: v.lengthSeconds ? 
          `${Math.floor(v.lengthSeconds/60)}:${String(v.lengthSeconds%60).padStart(2,'0')}` : '0:00',
        thumbnail: thumbUrl
      });
    }
    finalPlaylists.push({
      id: p.id,
      name: p.name,
      description: p.description,
      thumbnail: tracks.length > 0 ? tracks[0].thumbnail : '',
      tracks: tracks
    });
  }
  
  const fs = require('fs');
  fs.writeFileSync('default_playlists.json', JSON.stringify(finalPlaylists, null, 2));
  console.log('Finalizado! default_playlists.json criado.');
}

run();
