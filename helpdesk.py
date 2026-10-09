"""Учебный модуль для ревью. Исходная версия содержит дефекты."""
import json

tickets = []
next_id = 1

def reset():
    global next_id
    tickets.clear()
    next_id = 1

def create_ticket(title, user, tags=None):
    if tags is None:
        tags = []
    global next_id
    if title == "":
        raise ValueError("Пустой заголовок")
    ticket = {"id": next_id, "title": title, "user": user,
              "status": "open", "tags": tags}
    tickets.append(ticket)
    next_id += 1
    return ticket.copy()

def list_tickets(user):
    return [t for t in tickets if t["user"] == user]

def close_ticket(ticket_id):
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            ticket["status"] = "closed"
            return True
    return False

def closed_share():
    if not tickets:
        return 0.0
    closed = sum(t["status"] == "closed" for t in tickets)
    return closed / len(tickets) * 100
