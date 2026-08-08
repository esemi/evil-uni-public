# AWS

Минимум по AWS для python-backend: только то, что реально встречается в проде обычного web-сервиса.

## Как учить
- Завести free-tier аккаунт, поднять руками EC2 + S3 + RDS, чтобы пощупать
- Не лезть в 200+ сервисов — учить только то, что реально встречается в проде у обычного web-сервиса
- На собесе обычно спрашивают «какие сервисы использовал и зачем» + 1-2 глубоких вопроса. Цель — уметь объяснить trade-off’ы, а не зазубрить лимиты


## [Модель ответственности и регионы](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/global-infrastructure.html)
- Region vs Availability Zone vs Edge location
- Shared responsibility model: за что отвечает AWS, за что ты
- Почему мультизональный деплой ≠ мультирегиональный
- Latency и стоимость cross-AZ трафика


## [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
- User vs Role vs Policy
- Принцип least privilege
- Assume role, STS, временные креды
- IAM Role для EC2/ECS/Lambda — почему не нужны access keys внутри инстанса
- Где НЕЛЬЗЯ хранить AWS access keys (привет, git)
- Почему `*:*` в policy — это плохо


## Compute: EC2 / ECS / Fargate / Lambda
- EC2 — виртуалка, ты сам ставишь ОС и софт
- ECS — оркестрация контейнеров (аналог Kubernetes от AWS)
- Fargate — serverless контейнеры (без управления нодами)
- Lambda — serverless functions, до 15 минут, pay-per-invocation
- Когда выбирать что:
  - постоянная нагрузка → EC2 / ECS на EC2
  - переменная нагрузка → Fargate
  - редкие события, event-driven → Lambda
- Cold start у Lambda — почему это боль для latency-sensitive API
- Почему long-running задачи нельзя в Lambda


## [S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
- Object storage, не файловая система
- Bucket / key / versioning
- Storage classes: Standard / IA / Glacier — trade-off цена vs скорость
- Pre-signed URL — отдать клиенту прямой доступ без проксирования через бекенд
- Eventual consistency была раньше, теперь strong consistency
- Lifecycle policy — автоудаление/архивация
- Почему S3 нельзя использовать как файловую систему для random write


## RDS / Aurora / DynamoDB
- RDS — managed PostgreSQL/MySQL/etc. AWS делает бэкапы, патчи, failover
- Aurora — AWS-овый форк MySQL/Postgres с разделённым storage, быстрее и дороже
- DynamoDB — managed NoSQL key-value / document, single-digit ms latency
- Когда DynamoDB, а когда RDS:
  - известный access pattern, нужен горизонтальный scale → DynamoDB
  - сложные join-ы, аналитика, транзакции → RDS
- Read replicas — отдельный endpoint, eventual consistency
- Multi-AZ deployment — это про HA, не про scale
- Почему `SELECT *` в DynamoDB — это антипаттерн


## Очереди и стриминг: SQS / SNS / Kinesis / EventBridge
- SQS — pull-based очередь, at-least-once delivery
- SNS — pub/sub, push-based, fan-out
- SQS + SNS вместе — типовой fan-out паттерн (одно событие → много consumer’ов)
- Kinesis — стриминг данных, аналог Kafka, ordered shards
- EventBridge — event bus с фильтрацией, удобно для микросервисов
- Visibility timeout в SQS — почему он критичен (см. ACK/NOACK в software-engineering.md)
- Dead-letter queue — куда уходят сообщения, которые не смогли обработать
- Когда Kinesis, а когда SQS?


## VPC и сеть
- VPC = твоя виртуальная сеть в AWS
- Subnet: public vs private — где может торчать наружу
- Security Group (stateful) vs NACL (stateless)
- NAT Gateway — чтобы private subnet ходил в интернет
- VPC Endpoint — доступ к AWS-сервисам не через public интернет
- Почему RDS нельзя класть в public subnet


## Load balancing: ALB / NLB
- ALB — L7, HTTP/HTTPS, path/host routing
- NLB — L4, TCP/UDP, миллионы коннектов, низкая latency
- ALB умеет terminate TLS, sticky sessions, health checks
- Target group — куда роутить (EC2/ECS task/IP/Lambda)


## Observability: CloudWatch / X-Ray
- CloudWatch Logs — куда пишут все managed-сервисы и lambda по дефолту
- CloudWatch Metrics — стандартные + custom
- CloudWatch Alarms → SNS → PagerDuty/Slack
- X-Ray — distributed tracing (аналог Jaeger)
- Log Insights — query язык для логов
- Почему писать `print()` в Lambda — это нормально (и куда оно попадает)


## Деплой / IaC: CloudFormation / CDK / Terraform
- CloudFormation — родной IaC от AWS, YAML/JSON
- CDK — пишешь IaC на python/typescript, компилится в CloudFormation
- Terraform — multi-cloud, state хранится отдельно
- Terraform vs CloudFormation — про state и про vendor lock-in
- Stack vs Stack Set
- Drift — когда руками поменяли то, что управляется кодом


## Secrets: Secrets Manager / Parameter Store / KMS
- Secrets Manager — секреты с автоматической ротацией (дороже)
- SSM Parameter Store — параметры конфигурации + SecureString (дешевле)
- KMS — управление ключами шифрования, envelope encryption
- Почему секреты не хранят в env-переменных в plain text
- IAM role + Secrets Manager — стандартный паттерн доступа к БД из приложения


## Стоимость и типовые грабли
- Cross-AZ traffic — стоит денег, легко набежать
- NAT Gateway — дорогой, особенно по трафику
- Не выключенный EC2 / RDS — счёт месяцами
- S3 egress — выгрузка из AWS платная
- CloudWatch Logs retention по дефолту — бесконечно (= деньги)
- Reserved Instances vs Savings Plans vs On-Demand vs Spot
- Почему билл может неожиданно вырасти в 10 раз?


## Что почитать
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) — официальный гид по best practices, 6 столпов
- [The Open Guide to AWS](https://github.com/open-guides/og-aws) — community-driven, без маркетингового мусора
- [AWS in Plain English](https://expeditedsecurity.com/aws-in-plain-english/) — что какой сервис делает на пальцах


## Практика на один день
1. Поднять EC2 в public subnet, зайти по SSH, поставить nginx, открыть наружу через Security Group
2. Создать S3 bucket, залить файл через CLI, сгенерировать pre-signed URL
3. Создать RDS PostgreSQL в private subnet, подключиться к нему с EC2
4. Написать lambda на python, которая по триггеру из S3 (новый файл) пишет запись в DynamoDB
5. Найти всё созданное в Cost Explorer и УДАЛИТЬ, пока не натикало на тысячи денег
