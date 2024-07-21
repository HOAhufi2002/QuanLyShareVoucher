from flask import Blueprint

main_bp = Blueprint('main', __name__)
auth_bp = Blueprint('auth', __name__)
admin_bp = Blueprint('admin', __name__)
discount_bp = Blueprint('discount', __name__)
favorite_bp = Blueprint('favorite', __name__)
supplier_bp = Blueprint('supplier', __name__)
notification_bp = Blueprint('notification', __name__)
search_bp = Blueprint('search', __name__)
feedback_bp = Blueprint('feedback', __name__)

from .main import *
from .auth import *
from .admin import *
from .discount import *
from .favorite import *
from .supplier import *
from .notification import *
from .search import *
from .feedback import *
