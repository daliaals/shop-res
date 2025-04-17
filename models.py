from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Numeric, Enum, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

Base = declarative_base()


class UserRole(enum.Enum):
    employee = "employee"
    admin = "admin"
    shop_rep = "shop_rep"

class ShopStatus(enum.Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"
    locked = "locked"

class OrderStatus(enum.Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"
    preparing = "preparing"
    done = "done"
    

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False) 
    role = Column(Enum(UserRole), nullable=False)

class Shop(Base):
    __tablename__ = 'shops'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    rep_id = Column(Integer, ForeignKey('users.id'))
    status = Column(Enum(ShopStatus), default=ShopStatus.pending)

class ShopItem(Base):
    __tablename__ = 'shop_items'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Numeric, nullable=False)
    shop_id = Column(Integer, ForeignKey('shops.id'))

class Reservation(Base):
    __tablename__ = 'reservations'
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('users.id'))
    reservation_time = Column(DateTime, default=datetime.utcnow)

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('users.id'))
    shop_id = Column(Integer, ForeignKey('shops.id'))
    status = Column(Enum(OrderStatus), default=OrderStatus.pending)
    created_at = Column(DateTime, default=datetime.utcnow)

class OrderItem(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    shop_item_id = Column(Integer, ForeignKey('shop_items.id'))
    quantity = Column(Integer, nullable=False)
