# SSL Certificate FAQ

# Overview

This article answers common questions about **SSL certificate applications** and **Domain Control Validation (DCV)**.

For step-by-step instructions, please refer to the [**SSL Certificate Validation Methods Guide**](https://billing.raksmart.com/whmcs/index.php?rp=%2Fknowledgebase%2F739%2FSSL%E8%AF%81%E4%B9%A6%E9%AA%8C%E8%AF%81%E6%96%B9%E5%BC%8F%E6%8C%87%E5%8D%97.html&language=english).

---

## 1. Which email address receives the validation email?

The validation email is sent to the **DCV validation email address**, not the order contact email.

The Certificate Authority (CA) sends the validation email to the DCV email address selected during the application process (such as **[admin@yourdomain.com](mailto:admin@yourdomain.com)** or **[webmaster@yourdomain.com](mailto:webmaster@yourdomain.com)**) or to the domain's **WHOIS registrant email address**.

Please ensure that the selected mailbox is active and able to receive emails.

---

## 2. What validation methods are available? Can I change methods during validation?

Three validation methods are supported. You only need to complete one of them, and you may switch between methods at any time during the validation process.

| Validation Method | Best For | Notes |
| --- | --- | --- |
| **Email Validation** | Domain mailboxes that can receive emails | Supported addresses include **admin@**, **administrator@**, **webmaster@**, **hostmaster@**, **postmaster@**, or the **WHOIS registrant email** |
| **DNS Validation** | You manage the domain's DNS | Add the DNS record provided by the system. Validation will complete after DNS propagation. |
| **HTTP File Validation** | You can upload files to your website's document root | Upload the validation file to `/.well-known/pki-validation/`. **Wildcard certificates are not supported.** |

---

## 3. How long does it take to receive the validation email?

The validation email is usually delivered **within a few minutes**.

If you have not received it after **30 minutes**, please check the following:

- Make sure you are checking the correct DCV validation mailbox.
- Check your Spam, Junk, or Quarantine folders.
- Confirm that the mailbox is active.
- Verify that your domain's MX records are configured correctly.

If you still do not receive the email, we recommend switching to **DNS Validation** or **HTTP File Validation**, or submitting a support ticket for assistance.

---

## 4. Will incorrect country or postal code information affect validation?

No.

Domain Control Validation (DCV) only verifies that you have control over the domain. It is **not affected** by organization information such as the country or postal code.

However, we recommend providing accurate information for easier certificate management.

---

## 5. HTTP File Validation remains unverified. What should I check?

### (1) Each domain must be validated separately

If your certificate includes multiple domains (for example, **example.com** and **[www.example.com](http://www.example.com/)**), you must upload a validation file for each hostname.

For example:

```
http://example.com/.well-known/pki-validation/filename.txt

http://www.example.com/.well-known/pki-validation/filename.txt
```

---

### (2) Incorrect file path or file content

Please verify that:

- The validation file is located under:

```
/.well-known/pki-validation/
```

- The file content exactly matches the content provided by the system.
- The file is publicly accessible over HTTP and returns an **HTTP 200 OK** response.

---

### (3) CDN or Reverse Proxy

If your website is behind a CDN or reverse proxy:

- Temporarily bypass or disable caching for the validation path.
- Ensure that the Certificate Authority (CA) can access your origin server directly.

---

## 6. The certificate remains in **Pending** status for a long time

Please perform the following checks:

- Check your DCV status using the **Sectigo Order Status Checker**.
- Switch to another validation method and save the changes, then switch back and save again to trigger a new validation check.
- Confirm that your DNS records have fully propagated or that the validation file is publicly accessible.

After the DCV process is completed, the certificate is typically issued **within approximately 30 minutes**.

If the certificate has still not been issued after that, please submit a support ticket and include your order number for further assistance.

---

## 7. I entered incorrect information or accidentally clicked **Cancel**

### Pending

The domain usually cannot be modified while the certificate request is pending.

Please wait until the certificate is issued, or cancel the current order and submit a new application.

### Issued

You can use the **Replace** function in the control panel to reissue the certificate with the correct domain.

### Cancelled

Cancelled orders cannot be restored.

You will need to purchase the certificate again.

## 8: Why is my SSL certificate only valid for 199 days instead of the full service term?

According to industry standards, the maximum validity period for a single SSL certificate issuance is **199 days**.

If you purchase an SSL certificate with a service term longer than 199 days, the system will first issue a certificate that is valid for **199 days**.

Within **30 days before the certificate expires**, the system will automatically reissue (renew) a new certificate to cover the remaining service period.

**Please note:** After the certificate is reissued, you will need to **download and redeploy the new certificate** on your server. The new certificate will **not** be deployed automatically.

## 9. Do I need to redeploy the certificate after it is automatically reissued?

Yes.

Automatic certificate reissuance only generates a new certificate. It **does not** automatically deploy the new certificate to your server.

After the certificate has been reissued, please download the latest certificate and redeploy it to your server or web service to ensure your website continues to use HTTPS properly and to prevent service interruptions caused by an expired certificate.

---

## 10. Technical Support

If you need further assistance, please submit a support ticket through the Client Area and include the following information:

- Your SSL order number or domain name
- The validation method currently in use
- The troubleshooting steps you have already performed
- Any relevant error messages or screenshots

Providing this information will help us investigate and resolve your issue more efficiently.
