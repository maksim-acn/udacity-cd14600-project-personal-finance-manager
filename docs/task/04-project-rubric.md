---
title: "Software Architect"
source: "https://learn.udacity.com/nd772?version=1.0.9&partKey=cd14600&lessonKey=4f64d351-9b88-4b10-b845-8b3710a3c485&project=rubric"
author:
published:
created: 2026-05-04
description:
tags:
  - "clippings"
---
## Rubric

Use this project rubric to understand and assess the project criteria.

## Design Pattern Implementation

| Criteria | Submission Requirements |
| --- | --- |
| Implements Singleton Pattern for Balance Management | A Singleton Balance class is implemented correctly to ensure only one instance of the balance exists across the application. |
| Implements Adapter Pattern for External Transactions | An ExternalFreelanceIncome class and TransactionAdapter are included. Adapter correctly converts external data to internal Transaction objects. |
| Implements Observer Pattern for Low Balance Alerts and Balance Changes | A LowBalanceAlertObserver class is implemented and registered to the Balance class. Alert is triggered when balance falls below a defined threshold. Additionally, a PrintBalanace class is implemented and registered to the Balance Class. Balance is printed when a new transaction is applied. |
| Implements a Fourth Design Pattern (Student’s Choice) | Student selects and implements one additional design pattern that hasn’t been used already and documented the use clearly. |

## Industry Best Practices

| Criteria | Submission Requirements |
| --- | --- |
| Demonstrates Effective Unit Testing | Unit tests are written for Balance, Transaction, the Adapter, Observer, and custom pattern. Tests run without errors. |
| Project Runs Successfully and Applies Transactions | Running the main.py file simulates processing transactions and reflects updated balance and alerts. |
| Code is Clean, Modular, and Pythonic | Code follows PEP8 standards, uses idiomatic Python, and organizes classes by file and function. No large functions or excessive duplication. |

## Reflection

| Criteria | Submission Requirements |
| --- | --- |
| Student Provides a Reflection and Pattern Rationale | A short written reflection is included explaining the 4 patterns used, why each was chosen, and any trade-offs or challenges. |

## Suggestions to Make Your Project Stand Out

Add Undo/Redo Capability with Command Pattern - Implement command objects for applying transactions, and allow users to undo the last transaction.  
Add a Strategy for Budget Planning - Let users choose between budgeting strategies (e.g., "50/30/20 Rule", "Zero-Based Budgeting") and apply those strategies dynamically.  
Introduce Transaction Validation or Logging Decorator - Use a decorator to log each transaction or validate inputs before applying to the balance.

---

Click next to continue to the next lesson. You may return and submit or view a project at any time.