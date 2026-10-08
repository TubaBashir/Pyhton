import time
from typing import Callable, Dict, List, Any

# 1. THE EVENT CLASS
class Event:
    """Represents the data payload of a specific system action."""
    def __init__(self, name: str, data: Dict[str, Any]):
        self.name = name
        self.data = data
        self.timestamp = time.time()


# 2. THE EVENT DISPATCHER (THE HUB)
class OrderDispatcher:
    """Manages event registrations and routes incoming events to handlers."""
    def __init__(self):
        # Maps event names to a list of executable handler functions
        self._handlers: Dict[str, List[Callable[[Event], None]]] = {}

    def subscribe(self, event_name: str, handler: Callable[[Event], None]):
        """Registers an event handler for a specific event type."""
        if event_name not in self._handlers:
            self._handlers[event_name] = []
        self._handlers[event_name].append(handler)
        print(f"[System] Subscribed handler '{handler.__name__}' to event '{event_name}'.")

    def dispatch(self, event: Event):
        """Triggers all handlers registered to the incoming event type."""
        if event.name not in self._handlers or not self._handlers[event.name]:
            print(f"[System] Event '{event.name}' fired, but no handlers are listening.")
            return

        print(f"\n⚡ [Event Fired] '{event.name}' at {time.strftime('%H:%M:%S', time.localtime(event.timestamp))}")
        for handler in self._handlers[event.name]:
            # Execute the event handler and pass the event payload
            handler(event)


# 3. THE EVENT HANDLERS (THE SUBSCRIBERS)
def inventory_handler(event: Event):
    """Updates physical stock levels when an order is placed."""
    items = event.data.get("items", [])
    print(f"📦 [Inventory Management]: Allocating stock for items:")
    for item in items:
        print(f"   - {item['name']} (Quantity: {item['qty']})")


def notification_handler(event: Event):
    """Sends confirmation emails or SMS updates to the customer."""
    customer = event.data.get("customer_email")
    order_id = event.data.get("order_id")
    print(f"✉️  [Notification Service]: Sending confirmation email to {customer} for Order #{order_id}.")


def analytics_handler(event: Event):
    """Tracks metrics, total revenue, and sales patterns."""
    total = event.data.get("total_price", 0.0)
    print(f"📈 [Analytics Platform]: Logging revenue impact of +${total:.2f} to sales dashboard.")


def cancellation_handler(event: Event):
    """Handles reverse logistics and inventory restock upon cancellations."""
    order_id = event.data.get("order_id")
    reason = event.data.get("reason", "No reason provided")
    print(f"🛑 [Reverse Logistics]: Order #{order_id} cancelled due to: '{reason}'. Restocking items.")


# 4. SIMULATING THE PRODUCTION SYSTEM
if __name__ == "__main__":
    print("=== INITIALIZING SYSTEM SYSTEMS ===")
    dispatcher = OrderDispatcher()

    # Register multiple handlers to a single event type
    dispatcher.subscribe("order_placed", inventory_handler)
    dispatcher.subscribe("order_placed", notification_handler)
    dispatcher.subscribe("order_placed", analytics_handler)
    
    # Register a standalone handler for exceptions/cancellations
    dispatcher.subscribe("order_cancelled", cancellation_handler)

    print("\n=== SIMULATING USER TRAFFIC ===")

    # Mock Data: User places an order
    checkout_payload = {
        "order_id": 9942,
        "customer_email": "jane.doe@example.com",
        "items": [
            {"name": "Mechanical Keyboard", "qty": 1},
            {"name": "Ergonomic Mouse", "qty": 2}
        ],
        "total_price": 249.97
    }
    
    # Bundle data into an Event object and fire it
    order_event = Event("order_placed", checkout_payload)
    dispatcher.dispatch(order_event)

    # Delay simulation
    time.sleep(1)

    # Mock Data: User cancels a pending order
    cancellation_payload = {
        "order_id": 9942,
        "reason": "Accidental duplicate purchase"
    }
    
    cancel_event = Event("order_cancelled", cancellation_payload)
    dispatcher.dispatch(cancel_event)
