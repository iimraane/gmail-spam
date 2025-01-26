# README - Automated Email Sending Script

## **Script Description**

This script is designed to send a specified number of emails automatically, rotating sender email accounts to comply with the limitations of SMTP services such as Gmail. It is intended for testing purposes or friendly projects, but **must always be used ethically and with consent**.

---

## **Main Features**

- **Automated Sending**: Send a specified number of emails to a target address.
- **Rotating Senders**: Automatically cycles through configured SMTP accounts to distribute the load and avoid service limits.
- **Attachment Support**: Include a file (e.g., a video) as an attachment in the emails.
- **Simple Configuration**: User-friendly input prompts to specify the target address and email count during execution.

---

## **How It Works**

1. **Run the Script**: Execute the script using Python.
2. **Enter Target Email**: Provide the email address of the recipient.
3. **Choose Email Count**: Specify the number of emails to send.
4. **Automatic Rotation**: The script rotates between sender accounts to avoid exceeding daily limits (e.g., 500 emails/day for Gmail).
5. **Real-Time Updates**: Receive notifications for each successfully sent email.

---

## **Important: Responsible Use**

- **Use Only with Friends**: This script is meant for friendly or educational purposes, such as testing with informed consent. Misuse may violate laws and email service policies.
- **Gmail Limitation**: Gmail accounts have a daily sending limit of 500 emails.

**Always adhere to laws and ethical guidelines.**

---

## **SMTP Account Configuration**

### How to Obtain a Gmail Account for the Script

1. **Create a Gmail Account**: Sign up at [Gmail](https://mail.google.com).
2. **Enable Third-Party App Access**:
   - Log into your Gmail account.
   - Navigate to **Account Management > Security**.
   - Enable "Less secure app access" or generate an app password if the option is unavailable.
3. **Add Account to the Script**: Update the `smtp_senders` section with the email address, app password, and SMTP details.

### Using Other Email Providers

To use a non-Gmail address:
1. Find the SMTP settings of the provider (e.g., Outlook, Yahoo).
2. Add an entry in the `smtp_senders` list:
   ```python
   {
       "email": "address@example.com",
       "password": "password",
       "smtp_server": "smtp.example.com",
       "port": 587
   }
   ```
3. Test to ensure the provider supports bulk email sending via SMTP.

---

## **Attachment Instructions**

### Default Video Attachment
The script is configured to include a file named `video.mp4` as an attachment. If you wish to use this, ensure the file is located in the same directory as the script.

### Changing the Attachment
If you want to include a different file, modify the following line in the script:
```python
filename = "video.mp4"
```
Replace `video.mp4` with the name and extension of your desired file, e.g., `document.pdf` or `image.jpg`. Make sure the file exists in the specified path.

---

## **Example of Sender Rotation**

### Initial Configuration
Define multiple sender accounts in the `smtp_senders` list:
```python
smtp_senders = [
    {"email": "sender1@gmail.com", "password": "password1", "smtp_server": "smtp.gmail.com", "port": 587},
    {"email": "sender2@gmail.com", "password": "password2", "smtp_server": "smtp.gmail.com", "port": 587},
    {"email": "sender3@yahoo.com", "password": "password3", "smtp_server": "smtp.mail.yahoo.com", "port": 587},
]
```

### How it Works
The script automatically alternates between these accounts after sending an email or a group of emails. This ensures:
- Load distribution across accounts.
- Compliance with daily sending limits.

---

## **FAQ**

### What happens if an attachment is missing?
The script will continue sending emails even if the specified file is unavailable, and it will notify you of the issue.

### Does the script work without an attachment?
Yes, it will send emails containing only the text specified in the `body` variable.

### Can I stop the script mid-execution?
Yes, use `Ctrl+C` in the terminal to terminate the script.

### How many emails can I send?
The total depends on the number of configured sender accounts and their individual limits. For example:
- 3 Gmail accounts: 3 x 500 emails/day = 1500 emails/day.

---

## **Legal Disclaimer**

Misusing this script can lead to legal consequences and restrictions on your email accounts. **The author is not responsible for any inappropriate use of this script.**

Use this script only ethically and with the recipient's consent.

---

**License**

Please just don't steal my code..