# Z2

## A. Attackers & Motivation

### Noob

Non-capable and non-motivated to hack the system, just doing things wrong that can put a system in failure state

- users
- - think of your grandpa, who often clicks a button too many times or enters invalid values.

### Civilians

Non-capable and non-motivated to hack the system or users, but wanting to get services for free

- companies 
- - want to track user's behavior
- - want to weaken their concurrent 
- - avoid paying taxes / fees

- users
- - trying to manipulate the app to get services for free

### Dilettantes

Non-capable to hack system, but capable to trick users

- scammers
- - want to make user pay for their non-existing services
- - - by replacing MegaTravel site
- - - by making false companies
- - - by hacking user's account

### Hackers

Capable to hack system

- criminals 
- - want to steal user's PII and sell it
- - want to steal user's payment information and use it

## B. Assets

- user's PII (admin/confidentiality) -> attack will harm MegaTravel brand's image and the trust of their users. It will also require users immediate action to reduce the consequences which will compromise UI/UX. But this will not be detrimental to the company.
- user's payment information (no one / confidentiality) -> attack will harm MegaTravel brand's image and the trust of their users. Also, MegaTravel may be sued and required to pay a big fine. This can be detrimental to the company.
- user's behavior data (data team, should be anonymized / confidentiality, integrity) -> Competitors accessing this data will reduce MegaTravel's market advantage. The attack will harm MegaTravel's brand's image and the trust of its users. This can be detrimental to the company's position in the market.
- user's location (admin/confidentiality) -> attack will harm MegaTravel brand's image and the trust of their users. But this will not be detrimental to the company.
- company's turnover (admin + management staff/confidentiality) -> competitors accessing this data will reduce MegaTravel's market advantage. This will not be detrimental to the company but can enable competitors to catch up.
- servers handling users' requests (admin + DevOps / availability) -> Making company servers unavailable to the end-users will cause profit loss for the company and loss in user trust and satisfaction with our platform. 
- main database of the system (admin + DevOps / availability) -> Making company servers unavailable to the end-users will cause profit loss for the company and loss in user trust and satisfaction with our platform.

## C. & D. Attack Surface

![Stride](STRIDE.png)

1. Client connection with Web Server (MITM)
2. Web Server from the side of the client (attack on the API)
3. Web Server via SSH
4. DB from outside
5. DB from the server side (in case the Server is compromised)
6. Side API services from outside
7. Infrastructure from the Server side (in case the Server is compromised)
8. Physical attack on data center

![Surfaces](Surfaces.png)

## E. Threat and mitigation analysis

| Surface | Threat         | Attacker             | Mitigation                                                                                                                              |
|---------|----------------|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| 1.      | STI            | scammers             | HTTPS                                                                                                                                   |
| 2.      | S<br/>D<br/>E  | scammers             | Reliable headers, OAuth etc.<hr/>Fail2ban, Load Balancing etc.<hr/>Correct code                                                         |
| 3.      | TID            | criminals            | SSH vulnerabilities mitigation, SSH via VPN tunnel only                                                                                 |
| 4.      | TIDE           | criminals            | SSH vulnerabilities mitigation, SSH in same network only                                                                                |
| 5.      | I<hr/>TD<hr/>E | criminals            | -<hr/>Correct WS access rights (non admin)<hr/>Delegate Auth-Z to authorizer                                                            |
| 6.      | S<hr/>R        | scammers<hr/>clients | Aggregator recognize your service by API key, you recognize API by HTTPS certificate<hr/>agree on timely mutual exchange of information |
| 7.      | ID             | criminals            | Resource usage monitoring                                                                                                               |
|         | R              | clients, companies   | Proper logging of all actions                                                                                                           |
