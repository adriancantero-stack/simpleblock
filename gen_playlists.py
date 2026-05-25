import json
import uuid

playlists = [
    {
        "id": f"pl_{uuid.uuid4().hex[:8]}",
        "name": "Top Sertanejo",
        "description": "As mais tocadas do sertanejo e sofrência.",
        "thumbnail": "https://i.ytimg.com/vi/3Yf5VvPvHjQ/mqdefault.jpg",
        "tracks": [
            {"videoId": "3Yf5VvPvHjQ", "title": "Ana Castela - Nosso Quadro", "uploader": "AgroPlay", "durationText": "2:54", "thumbnail": "https://i.ytimg.com/vi/3Yf5VvPvHjQ/mqdefault.jpg"},
            {"videoId": "OgE00Qz9T0s", "title": "Gusttavo Lima - Termina Comigo Antes", "uploader": "Gusttavo Lima", "durationText": "3:10", "thumbnail": "https://i.ytimg.com/vi/OgE00Qz9T0s/mqdefault.jpg"},
            {"videoId": "5fDPznvFyU4", "title": "Marília Mendonça - Leão", "uploader": "Marília Mendonça", "durationText": "2:46", "thumbnail": "https://i.ytimg.com/vi/5fDPznvFyU4/mqdefault.jpg"},
            {"videoId": "FmPJh3Yz8uE", "title": "Jorge & Mateus - Todo Seu", "uploader": "Jorge e Mateus", "durationText": "2:52", "thumbnail": "https://i.ytimg.com/vi/FmPJh3Yz8uE/mqdefault.jpg"}
        ]
    },
    {
        "id": f"pl_{uuid.uuid4().hex[:8]}",
        "name": "Funk Hits",
        "description": "Os maiores hits do funk brasileiro.",
        "thumbnail": "https://i.ytimg.com/vi/dDuAQT4mLW8/mqdefault.jpg",
        "tracks": [
            {"videoId": "dDuAQT4mLW8", "title": "Pedro Sampaio - DANÇARINA", "uploader": "Pedro Sampaio", "durationText": "1:50", "thumbnail": "https://i.ytimg.com/vi/dDuAQT4mLW8/mqdefault.jpg"},
            {"videoId": "S0LjqRGFiVo", "title": "Anitta - Envolver", "uploader": "Anitta", "durationText": "3:13", "thumbnail": "https://i.ytimg.com/vi/S0LjqRGFiVo/mqdefault.jpg"},
            {"videoId": "R4tYQjE2R4w", "title": "MC Ryan SP - Let's Go 4", "uploader": "GR6 Explode", "durationText": "10:11", "thumbnail": "https://i.ytimg.com/vi/R4tYQjE2R4w/mqdefault.jpg"},
            {"videoId": "O_D1C7eT0xQ", "title": "MC Kevin o Chris - Tá OK", "uploader": "Dennis", "durationText": "1:58", "thumbnail": "https://i.ytimg.com/vi/O_D1C7eT0xQ/mqdefault.jpg"}
        ]
    },
    {
        "id": f"pl_{uuid.uuid4().hex[:8]}",
        "name": "Paredão Forró",
        "description": "Só as melhores do forró e piseiro.",
        "thumbnail": "https://i.ytimg.com/vi/V4e5-qXCxYg/mqdefault.jpg",
        "tracks": [
            {"videoId": "V4e5-qXCxYg", "title": "Zé Vaqueiro - Letícia", "uploader": "Zé Vaqueiro", "durationText": "3:02", "thumbnail": "https://i.ytimg.com/vi/V4e5-qXCxYg/mqdefault.jpg"},
            {"videoId": "GNxaH_ioRj8", "title": "Wesley Safadão - Tu Tava na Revoada", "uploader": "Wesley Safadão", "durationText": "2:49", "thumbnail": "https://i.ytimg.com/vi/GNxaH_ioRj8/mqdefault.jpg"},
            {"videoId": "MZQ5a8bFJbg", "title": "Xand Avião - Balanço da Rede", "uploader": "Xand Avião", "durationText": "2:34", "thumbnail": "https://i.ytimg.com/vi/MZQ5a8bFJbg/mqdefault.jpg"},
            {"videoId": "l3X2wR_7H0o", "title": "João Gomes - Meu Pedaço de Pecado", "uploader": "João Gomes", "durationText": "2:45", "thumbnail": "https://i.ytimg.com/vi/l3X2wR_7H0o/mqdefault.jpg"}
        ]
    },
    {
        "id": f"pl_{uuid.uuid4().hex[:8]}",
        "name": "Pop Internacional",
        "description": "Hits do pop mundial.",
        "thumbnail": "https://i.ytimg.com/vi/q3zqJs7JUCQ/mqdefault.jpg",
        "tracks": [
            {"videoId": "q3zqJs7JUCQ", "title": "Taylor Swift - Anti-Hero", "uploader": "Taylor Swift", "durationText": "5:09", "thumbnail": "https://i.ytimg.com/vi/q3zqJs7JUCQ/mqdefault.jpg"},
            {"videoId": "XXYlFuWiqLg", "title": "The Weeknd - Save Your Tears", "uploader": "The Weeknd", "durationText": "4:08", "thumbnail": "https://i.ytimg.com/vi/XXYlFuWiqLg/mqdefault.jpg"},
            {"videoId": "oygrmJFKYZY", "title": "Dua Lipa - Don't Start Now", "uploader": "Dua Lipa", "durationText": "3:02", "thumbnail": "https://i.ytimg.com/vi/oygrmJFKYZY/mqdefault.jpg"},
            {"videoId": "DyDfgMOUjCI", "title": "Billie Eilish - bad guy", "uploader": "Billie Eilish", "durationText": "3:25", "thumbnail": "https://i.ytimg.com/vi/DyDfgMOUjCI/mqdefault.jpg"}
        ]
    },
    {
        "id": f"pl_{uuid.uuid4().hex[:8]}",
        "name": "Lo-Fi Chill",
        "description": "Para relaxar e focar.",
        "thumbnail": "https://i.ytimg.com/vi/jfKfPfyJRdk/mqdefault.jpg",
        "tracks": [
            {"videoId": "jfKfPfyJRdk", "title": "lofi hip hop radio - beats to relax/study to", "uploader": "Lofi Girl", "durationText": "LIVE", "thumbnail": "https://i.ytimg.com/vi/jfKfPfyJRdk/mqdefault.jpg"},
            {"videoId": "5qap5aO4i9A", "title": "lofi hip hop radio - beats to sleep/chill to", "uploader": "Lofi Girl", "durationText": "LIVE", "thumbnail": "https://i.ytimg.com/vi/5qap5aO4i9A/mqdefault.jpg"},
            {"videoId": "MCkTebktHVc", "title": "Chillhop Radio - jazzy & lofi hip hop beats", "uploader": "Chillhop Music", "durationText": "LIVE", "thumbnail": "https://i.ytimg.com/vi/MCkTebktHVc/mqdefault.jpg"}
        ]
    },
    {
        "id": f"pl_{uuid.uuid4().hex[:8]}",
        "name": "Reggaeton Caliente",
        "description": "As melhores do reggaeton.",
        "thumbnail": "https://i.ytimg.com/vi/kTlv5_Bs8aw/mqdefault.jpg",
        "tracks": [
            {"videoId": "kTlv5_Bs8aw", "title": "Bad Bunny - Tití Me Preguntó", "uploader": "Bad Bunny", "durationText": "4:05", "thumbnail": "https://i.ytimg.com/vi/kTlv5_Bs8aw/mqdefault.jpg"},
            {"videoId": "91BU7o_0oq0", "title": "Karol G - PROVENZA", "uploader": "Karol G", "durationText": "3:30", "thumbnail": "https://i.ytimg.com/vi/91BU7o_0oq0/mqdefault.jpg"},
            {"videoId": "p3cGzt_YJgY", "title": "Rauw Alejandro - Todo de Ti", "uploader": "Rauw Alejandro", "durationText": "3:20", "thumbnail": "https://i.ytimg.com/vi/p3cGzt_YJgY/mqdefault.jpg"},
            {"videoId": "7dMcdD1-w1c", "title": "Bizarrap & Quevedo - Bzrp Music Sessions, Vol. 52", "uploader": "Bizarrap", "durationText": "3:18", "thumbnail": "https://i.ytimg.com/vi/7dMcdD1-w1c/mqdefault.jpg"}
        ]
    },
    {
        "id": f"pl_{uuid.uuid4().hex[:8]}",
        "name": "Hip-Hop / Rap",
        "description": "Batidas pesadas e rimas afiadas.",
        "thumbnail": "https://i.ytimg.com/vi/uxpDa-c-4Mc/mqdefault.jpg",
        "tracks": [
            {"videoId": "uxpDa-c-4Mc", "title": "Drake - God's Plan", "uploader": "Drake", "durationText": "5:56", "thumbnail": "https://i.ytimg.com/vi/uxpDa-c-4Mc/mqdefault.jpg"},
            {"videoId": "UceaB4D0jpo", "title": "Post Malone - rockstar", "uploader": "Post Malone", "durationText": "4:01", "thumbnail": "https://i.ytimg.com/vi/UceaB4D0jpo/mqdefault.jpg"},
            {"videoId": "TVkqQcsO24Y", "title": "Kendrick Lamar - HUMBLE.", "uploader": "Kendrick Lamar", "durationText": "3:03", "thumbnail": "https://i.ytimg.com/vi/TVkqQcsO24Y/mqdefault.jpg"},
            {"videoId": "Ndqw_N5uIe0", "title": "Travis Scott - SICKO MODE", "uploader": "Travis Scott", "durationText": "5:22", "thumbnail": "https://i.ytimg.com/vi/Ndqw_N5uIe0/mqdefault.jpg"}
        ]
    }
]

with open('default_playlists.json', 'w', encoding='utf-8') as f:
    json.dump(playlists, f, ensure_ascii=False, indent=2)
print("done")
