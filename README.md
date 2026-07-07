# Personal Blogging API

Acest proiect reprezintă un API RESTful simplu, dezvoltat în **Flask**, care permite gestionarea postărilor de pe un blog personal prin operații de tip CRUD (Create, Read, Update, Delete).

## 🚀 Funcționalități
- **Create**: Adăugarea unei postări noi cu titlu, conținut, categorie și tag-uri.
- **Read**: Vizualizarea tuturor postărilor sau a unei postări specifice prin ID.
- **Update**: Modificarea detaliilor unei postări existente.
- **Delete**: Ștergerea unei postări din baza de date temporară.
- **Search**: Filtrarea postărilor după un termen specific în titlu sau conținut.

## 🛠 Tehnologii utilizate
- **Python 3**
- **Flask** (Framework pentru API)
- **Postman/cURL** (pentru testarea endpoint-urilor)

## 📦 Instalare și Rulare

1. **Clonează repository-ul:**
   ```bash
   git clone <link-ul-proiectului-tau>
   cd <numele-folderului>
   ```

2. Creează și activează un mediu virtual:
  ``` bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

3. Instalează dependențele:
  ``` bash 
  pip install flask
  ```

4. Pornește serverul:
  ``` bash
  python3 main.py
  Serverul va rula la adresa: http://127.0.0.1:5000
