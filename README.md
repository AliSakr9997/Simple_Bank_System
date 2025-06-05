
# 💳 Simple Console Banking System (Python)

A command-line banking system where users can log in and manage their balance. The program supports password management, balance inquiries, deposits, withdrawals, and money transfers between users.

---

## 📌 Features

- User authentication (username and password)
- Change password
- Check account balance
- Deposit money
- Withdraw money
- Transfer money to another user

---

## 🚀 How to Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/console-banking.git
   cd console-banking
    ````

2. **Run the script:**

   ```bash
   python banking_system.py
   ```

> 💡 Requires **Python 3.x**

---

## 👥 Predefined Users

| Username | Password   | Balance |
| -------- | ---------- | ------- |
| ali      | vli21\_XO  | 4300    |
| ebrahim  | monir-sakr | 6500    |

---

## 🧠 How It Works

1. Users are prompted to **log in** using their username and password.
2. After a successful login, users can select from the following operations:

   * `1`: Change password
   * `2`: Check balance
   * `3`: Deposit money
   * `4`: Withdraw money
   * `5`: Transfer money to another user
3. The system performs basic validation:

   * Maximum 3 login attempts
   * Validates available balance before withdrawal or transfer
   * Prevents sending money to oneself
   * Prevents reuse of the same password

---

## 🔐 Security Notes

* This is a basic educational script.
* All data is stored in memory and resets when the program restarts.
* No encryption or persistent storage is used.

---

## 🛠 Built With

* Python 3
* Standard I/O

---

## 👤 Author

Feel free to connect if you have any questions or want to collaborate on similar projects!  
- **Name:** Ali Ebrahim Monir Sakr  
- **Email:** alimonirsakr@gmail.com  
- **LinkedIn:** [Ali Monir Sakr](https://www.linkedin.com/in/ali-monir-sakr)  

---
