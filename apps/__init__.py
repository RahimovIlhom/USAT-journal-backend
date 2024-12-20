from .accounts.apps import AccountsConfig
from .archive.apps import ArchiveConfig
from .articles.apps import ArticlesConfig
from .authors.apps import AuthorsConfig
from .categories.apps import CategoriesConfig
from .journals.apps import JournalsConfig
from .reviews.apps import ReviewsConfig

__all__ = [
    "AccountsConfig",
    "ArchiveConfig",
    "ArticlesConfig",
    "AuthorsConfig",
    "CategoriesConfig",
    "JournalsConfig",
    "ReviewsConfig",
]