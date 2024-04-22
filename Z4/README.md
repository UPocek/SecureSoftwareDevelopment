# Z4

## Uros

## Tamara

## Alex

### ████ - Credit agreement analysis tool

1. That's a real life project from Upwork. It is based on the startup idea of █████████, an american business student.
    
    In a few words, the idea is to convert standard credit agreements into Excel tables using ChatGPT. 
    Since clients are providing personal data as credit agreements - code need to be secure and reliable.

    On the other hand this work was made very fast and just for 15$/hr
    (what is very cheap price for a work with screen recorder, I would say). So the quality of code should be low.
    Let's find bugs! 
2. █████████ - founder and r&d. Aleksandr Mishutkin - developer.
3. Defects found by **Bandit** tool: 
    
    | Issue                                                                                                    | Severity | Confidence | CWE     | Location                                                 | Code Example                                                                  | Solution                                                |
    |----------------------------------------------------------------------------------------------------------|----------|------------|---------|----------------------------------------------------------|-------------------------------------------------------------------------------|---------------------------------------------------------|
    | [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes. | Low      | High       | CWE-330 | [auth_views.py:37:56](.\ParsingAPI\auth_views.py:37:56)  | `user.username = request.POST['email'] + str(random.randint(100000, 999999))` | Use a cryptographically secure random number generator. |
    | [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes. | Low      | High       | CWE-330 | [auth_views.py:39:24](.\ParsingAPI\auth_views.py:39:24)  | `safe_code = random.randint(100000, 999999)`                                  | Use a cryptographically secure random number generator. |
    | [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes. | Low      | High       | CWE-330 | [auth_views.py:41:28](.\ParsingAPI\auth_views.py:41:28)  | `safe_code = random.randint(100000, 999999)`                                  | Use a cryptographically secure random number generator. |
    | [B113:request_without_timeout] Requests call without timeout                                             | Medium   | Low        | CWE-400 | [email_service.py:29:15](.\Utils\email_service.py:29:15) | `response = requests.post(url, headers=headers, data=json.dumps(payload))`    | Set a timeout value for the requests call.              |
    | [B113:request_without_timeout] Requests call without timeout                                             | Medium   | Low        | CWE-400 | [email_service.py:74:15](.\Utils\email_service.py:74:15) | `response = requests.post(url, headers=headers, data=json.dumps(payload))`    | Set a timeout value for the requests call.              |

    My own concerns:
    1. I haven't left password and API keys in the code, but some non-critical credentials are still present:
       1. Sendgrid email
       2. Allowed hosts
       3. DB host!!! in `settings.py`
       4. My and █████████'s email in the `email_service.py` (we were in a cc for all messages)
    
       All this values could be moved to envs.
   2. The files are saved to S3, but they are also stored on disc.
      The files' size is not controlled, so DDOS attack can easily use all the memory.
   3. Django default password security settings
   4. Email validation code have no timeout
5. Advises:
   1. Don't outstaff work with sensitive finances to the Upwork
   2. More credentials to the ENV variables (use CI/CD, instead of manual deployment)
   3. More advanced password policies
   4. More advanced 2FA policies
   5. Or use SaaS authorizer instead
   6. Use `Tempfile` or other library to manage file upload
   7. `Fail2ban`. The problem is not fully described here, but it's really needed, trust me
   8. Make corporate emails for developers, and use them from ENVs
6. 40 minutes (including Bandit installation and logging in to my Upwork account).
   But project is not big, and I'm familiar with it
