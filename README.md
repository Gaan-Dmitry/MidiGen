# 🎹 MidiGen: JSON to MIDI Converter

**MidiGen** — это легковесное локальное приложение, которое превращает структурированные JSON-данные в полноценные MIDI-файлы. Идеально подходит для музыкантов, использующих DAW (REAPER, Ableton, FL Studio), чтобы быстро переносить сгенерированные ИИ партии в свои проекты.

---

## ✨ Возможности

| Функция | Описание |
| :--- | :--- |
| 📝 **Мгновенная конвертация** | Просто вставь JSON и нажми кнопку. |
| 🎲 **Эффект Humanize** | Случайные микро-отклонения силы нажатия (`±5` velocity) и тайминга (`±0.01` сек) для "живого" звучания. |
| 📂 **Прямой экспорт** | Файл `output.mid` сохраняется сразу в папке с программой. |
| 🛠 **Простая структура** | Поддержка полей: `p` (pitch), `t` (time), `d` (duration), `v` (velocity). |

---

## 🚀 Быстрый старт

Для корректной работы рекомендуется использовать виртуальное окружение.

### 1. Клонирование репозитория
```bash
git clone https://github.com/Gaan-Dmitry/MidiGen.git
cd MidiGen
```

### 2. Настройка окружения
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 4. Запуск приложения
```bash
python main.py
```

---

## 🤖 Промпт для генерации данных (AI)

Чтобы получить данные, которые MidiGen гарантированно поймет, используйте этот шаблон в чате с **Gemini**, **Qwen Coder** или **Claude**:

> **Скопируй и отправь этот промпт:**
```
 "Напиши MIDI-данные в формате JSON для следующего запроса: *[ТВОЙ ЗАПРОС, например: Арпеджио в Am]*.
 Используй строго структуру массива объектов:
`[{"p": 60, "t": 0.0, "d": 0.5, "v": 80}]`
Где: `p`=нота (MIDI ID), `t`=время начала (доли), `d`=длительность, `v`=velocity.
Выдай только чистый JSON код без лишнего текста."
````
---

## 👨‍💻 Об авторе и инструментах

**Разработчик:** [Dmitry Gaan](https://github.com/Gaan-Dmitry)  
*Я — музыкант и разработчик. Люблю автоматизацию творческих процессов. MidiGen был создан, чтобы убрать рутину из процесса создания музыки в REAPER.*

### 🔗 Контакты

[![GitHub](https://img.shields.io/badge/GitHub-Gaan--Dmitry-181717?style=flat&logo=github)](https://github.com/Gaan-Dmitry)  
[![Telegram](https://img.shields.io/badge/Telegram-@Gaan_Dmitry-24A1DE?style=flat&logo=telegram)](https://t.me/Gaan_Dmitry)  
[![VKontakte](https://img.shields.io/badge/VK-gaan_dmitry-0077FF?style=flat&logo=vk)](https://vk.com/gaan_dmitry)

### 🤖 ИИ-помощники в разработке

Этот проект создан при поддержке современных языковых моделей:

*   **🌟 Qwen Coder (Alibaba Cloud)**  
    Специализированная модель, использовавшаяся для генерации и оптимизации кода.  
    [Официальный сайт](https://qwenlm.github.io/) • [GitHub](https://github.com/QwenLM)

*   **💎 Gemini (Google DeepMind)**  
    Помогал в проектировании архитектуры, логики "Humanize" и написании документации.  
    [Официальный сайт](https://gemini.google.com/) • [Документация Google AI](https://ai.google.dev/)

---

## 📄 Лицензия

Распространяется под лицензией **MIT**. Подробнее см. файл [LICENSE](LICENSE).
