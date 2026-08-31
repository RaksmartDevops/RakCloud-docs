# Business Email FAQ

## Overview

This article answers common questions about login, administration, and configuration for RAKsmart enterprise email.

## 1. Are mail servers in China or the United States?

Servers are distributed globally. Access from overseas uses overseas nodes; access from China uses domestic nodes to improve delivery speed and stability in each region.

## 2. Is there a separate administrator account?

Yes. After provisioning, you receive administrator credentials on the platform.

- Login URL: [https://mail.chengmail.cn](https://mail.chengmail.cn/)
- The page opens in user login mode by default
- Click Switch to administrator login on the right side of the welcome message
- Log in with the administrator account

## 3. I forgot the enterprise email administrator password

Administrator passwords can only be reset from the backend. Self-service reset is not available. Open a support ticket with your domain or email product order details.

## 4. Enterprise email help center

- <https://mail.chengmail.cn/help/index.php?_m=articleview&_a=view>
- [Chinese user manual](https://mail.chengmail.cn/help/index.php?_m=articleview&_a=view&category_id=044f972f81a3be258c2c35e8ae6ee6d8&lang=zh_CN)

## 5. How do I set up SMTP? What about MX, CNAME, and TXT records?

Log in to the enterprise email admin panel and open Domain management or Mailbox settings. The system shows the records required for your domain:

| Record type | Purpose |
| --- | --- |
| MX | Mail routing |
| TXT (SPF) | Anti-spoofing and deliverability |
| CNAME | Required for some features, as shown in the panel |
| SMTP | Outbound server and port, as shown in the panel |

Values are domain-specific. Use what the admin panel displays. If you cannot find them, open a ticket with your domain name.

## 6. How do I create and manage user mailboxes?

After logging in as administrator at [mail.chengmail.cn](https://mail.chengmail.cn/), you can create or delete mailboxes, assign quotas, and configure aliases and forwarding. See the [enterprise email help center](https://mail.chengmail.cn/help/index.php?_m=articleview&_a=view&category_id=044f972f81a3be258c2c35e8ae6ee6d8&lang=zh_CN) for details.

## 7. Technical support

Open a support ticket from the client area with your domain, a description of the issue, and steps already tried with screenshots.
