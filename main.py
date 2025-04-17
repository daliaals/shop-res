from database import Base, engine
from models.models import OrderItem, Order, Reservation, ShopItem, Shop, User, OrderStatus, ShopStatus, UserRole

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("All tables created successfully.")