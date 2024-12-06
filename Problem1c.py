# Role and Permissions Mapping
class RolePermissions:
    def __init__(self):
        self.permissions = {
            "Client": ["View Account Balance", "View Portfolio", "Contact Advisor"],
            "PremiumClient": ["View Account Balance", "View Portfolio", "Modify Portfolio", "Contact Planner"],
            "Employee": ["View Account Balance", "View Portfolio"],
            "FinancialAdvisor": ["View Account Balance", "View Portfolio", "View Instruments"],
            "FinancialPlanner": ["View Account Balance", "View Portfolio", "View Instruments", "Access Money Market"],
            "Teller": ["View Account Balance", "View Portfolio", "Process Transactions"],
            "Admin": ["Manage Roles", "Full Access"]
        }

    def get_permissions(self, role):
        """Return the list of permissions for the specified role."""
        return self.permissions.get(role, [])

def display_permissions(role):
    role_permissions = RolePermissions()
    permissions = role_permissions.get_permissions(role)
    if not permissions:
        return f"No permissions found for the role: {role}"
    return f"Permissions for {role}: " + ", ".join(permissions)
