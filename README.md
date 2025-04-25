# OCR + LLM Q&A System

This project allows users to upload an image (like a passport), extract text from it using OCR, and then ask questions about the extracted content using a Large Language Model (LLM).

## 🔧 Features

- 📷 OCR (Optical Character Recognition) using `easyocr`
- 🧠 Natural Language Q&A powered by `llama-cpp-python`
- 📁 Frontend built with React and Axios
- 🚀 Backend using FastAPI
- ⏱️ Handles long model processing time with progress indication (up to 6 minutes)

---

## 📁 Project Structure


---

## 🔍 What It Does

- Accepts an image + question via frontend.
- Extracts OCR text using `easyocr`.
- Passes text and question to the LLM (`llama-cpp`).
- Returns both OCR output and the model-generated answer.

---

## 🧪 Example Output

**Image Input**: Passport of a fictional user  
**OCR Extracted Text**:

      1.Nationality: British

      2.Passport number: 12345-01234



---

## 📊 Performance Log (LLM)

                  llama_perf_context_print:        load time = 176335.41 ms
                  llama_perf_context_print: prompt eval time = 19964.92 ms / 18 tokens
                  llama_perf_context_print:        eval time = 57790.91 ms / 93 runs
                  llama_perf_context_print:       total time = 77822.80 ms / 111 tokens


This means the total LLM response time can be ~78 seconds depending on input complexity.

---

## ⏳ Progress Handling

The frontend now includes a **progress bar** that tracks waiting time for up to 6 minutes (~360 seconds), giving users a better experience during long model inference.

---

## 🧠 Notes

- Ensure your system supports AVX2 for running `llama-cpp`.
- Running on CPU can be slow. Consider GPU acceleration if supported.
- Use smaller models or quantized `.gguf` formats for faster inference.

---

## 📬 Feedback

Pull requests and issues are welcome! Let’s improve OCR+LLM together 🚀
