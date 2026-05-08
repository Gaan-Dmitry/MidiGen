# 🎹 JSON to MIDI Converter

Простое локальное приложение для конвертации JSON-нот в MIDI-файл с эффектом **humanize**.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Возможности

- 📝 Вставка JSON с нотами (поля: `p` — питч, `t` — время, `d` — длительность, `v` — velocity)
- 🎛️ Кнопка конвертации в MIDI
- 🎲 **Humanize**: случайные отклонения velocity (±5) и времени (±0.01 сек)
- 💾 Сохранение `output.mid` в папке с программой

## 🚀 Установка

```bash
# 1. Клонируйте репозиторий или скачайте файлы
git clone <your-repo-url>
cd json-to-midi

# 2. Установите зависимости
pip install -r requirements.txt

# 3. Запустите приложение
python main.py
```

## 📖 Формат JSON

```json
[
  {"p": 60, "t": 0.0, "d": 0.5, "v": 80},
  {"p": 64, "t": 0.5, "d": 0.5, "v": 75},
  {"p": 67, "t": 1.0, "d": 1.0, "v": 85}
]
```

## 🤖 ИИ-ассистент

При разработке использовался **Qwen Coder** — мощная языковая модель для генерации кода.

🔗 Ссылки:
- [Официальный сайт Qwen](https://qwenlm.github.io/)
- [Hugging Face — Qwen](https://huggingface.co/Qwen)
- [GitHub — Qwen](https://github.com/QwenLM)

---

## 📄 Лицензия

Распространяется под лицензией **MIT**. Подробнее см. файл [LICENSE](LICENSE).
