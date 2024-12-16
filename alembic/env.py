from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Import models from each service
from services.authentication_service.app.models.user import User
from services.expense_tracking_service.app.models.expense import Expense
from services.spending_recommendations_service.app.models.recommendation import Recommendation
from services.savings_goals_service.app.models.goal import Goal
from services.financial_health_reports_service.app.models.report import HealthReport
from services.ai_financial_advice_service.app.models.advice import FinancialAdvice

# Alembic config object to access .ini settings
config = context.config

# Set up logging (optional)
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Consolidate all metadata (from all services)
target_metadata = (
    User.metadata
    .extend(Expense.metadata)
    .extend(Recommendation.metadata)
    .extend(Goal.metadata)
    .extend(HealthReport.metadata)
    .extend(FinancialAdvice.metadata)
)

def run_migrations_offline() -> None:
    """Run migrations in offline mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in online mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

# Additional method to auto-generate migrations when models change (table creation, modification, deletion)
def generate_migration() -> None:
    """Generate migration script based on model changes."""
    from alembic.command import revision
    from alembic.config import Config

    alembic_cfg = Config("alembic.ini")  # Make sure you have alembic.ini configured in your project
    revision(alembic_cfg, autogenerate=True, message="Auto-generated migration")
