ROLE_PERMISSIONS = {
    "Client": ["View Account Balance", "View Portfolio"],
    "PremiumClient": ["View Account Balance", "View Portfolio", "Modify Portfolio"],
    "FinancialAdvisor": ["View Client Data", "View Instruments"],
    "FinancialPlanner": ["View Client Data", "View Instruments", "Access Money Market"],
    "Teller": ["Process Transactions", "View Limited Client Data"],
    "Admin": ["Full System Access"]
}

def display_authorized_options(role):
    options = ROLE_PERMISSIONS.get(role, [])
    if not options:
        return f"No authorized options for the role: {role}"
    return f"Authorized options for {role}:\n- " + "\n- ".join(options)
