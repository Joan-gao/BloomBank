from contextlib import contextmanager
from _decimal import Decimal
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import extract
from model.model import *
from datetime import datetime, date
import hashlib
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from collections import defaultdict
import logging
import json

# 配置数据库 URI
DATABASE_URI = 'mysql+pymysql://root:root123456@127.0.0.1:3306/Finance'

# 创建 SQLAlchemy 引擎
engine = create_engine(DATABASE_URI, echo=True)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# 初始化数据库
logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def init_db():
    Base.metadata.create_all(bind=engine)


init_db()
# session = SessionLocal()

SessionFactory = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = SessionFactory()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


categories = {
    1: "Salary income",
    2: "Bonus income",
    3: "Investment Income income",
    4: "Other Income income",
    5: "Business income",
    6: "Part-time Job income",
    7: "Buying and Selling income",
    8: "Housing expense",
    9: "Food expense",
    10: "Transportation expense",
    11: "Entertainment expense",
    12: "Utilities expense",
    13: "Health expense",
    14: "Insurance expense",
    15: "Education expense",
    16: "Other Expenses expense",
    17: "Investment Expens expense",
    18: "Shopping expense",
    19: "Grocery expense"
}
# Generate Password Hash


def add_transaction(user_id, category_id, transaction_date, description, amount, note='', is_shown=0):
    try:
        with session_scope() as session:
            new_transaction = Transaction(
                user_id=user_id,
                category_id=category_id,
                transaction_date=transaction_date,
                description=description,
                amount=amount,
                note=note,
                is_shown=is_shown
            )

            session.add(new_transaction)
            return new_transaction
    except Exception as e:
        logging.error("Error occurred while adding transaction: %s", e)
        raise


def update_transaction(user_id, transaction_date, amount, new_info_dict):
    with session_scope() as session:
        transaction = session.query(Transaction).filter_by(
            user_id=user_id, transaction_date=transaction_date, amount=amount).one_or_none()
        if transaction is None:
            return None

        for key, value in new_info_dict.items():
            if hasattr(transaction, key) and transaction[key] != "None":
                setattr(transaction, key, value)

        session.commit()
        return transaction


def format_transaction(transaction):
    return f"Transaction(id={transaction.transaction_id}, user_id={transaction.user_id}, category_id={transaction.category_id}, transaction_date={transaction.transaction_date}, description='{transaction.description}', amount={transaction.amount})"


def format_transactions(transactions):
    return [format_transaction(transaction) for transaction in transactions]


def search_transaction(user_id, transaction_date, amount):
    with session_scope() as session:
        transaction = session.query(Transaction).filter_by(
            user_id=user_id, transaction_date=transaction_date, amount=amount).all()
        if transaction is None:
            return None

        session.commit()
        return format_transactions(transaction)


def remove_transaction(user_id, transaction_date, amount):
    with session_scope() as session:
        print(user_id, transaction_date, amount)
        transaction = session.query(Transaction).filter_by(
            user_id=user_id, transaction_date=transaction_date, amount=amount).one_or_none()
        if transaction is None:
            return None

        transaction_info = format_transaction(
            transaction) if transaction != None else None
        session.delete(transaction)
        session.commit()
        return transaction_info


def generate_hash(input_string):
    # 创建 SHA-256 哈希对象
    sha256 = hashlib.sha256()

    # 更新哈希对象以包括输入字符串
    sha256.update(input_string.encode('utf-8'))

    # 获取哈希值的十六进制表示
    hash_hex = sha256.hexdigest()

    return hash_hex


def categorize_transactions(transactions, categories):
    # Initialize dictionaries to hold counts and category types
    income = {}
    expense = {}
    total_cost = {}
    # Count transactions per category_id, using the category name as the key
    for transaction in transactions:
        category_id = transaction['category_id']
        if category_id in categories:
            # Extract category name and type from the categories dictionary
            category_name, category_type = categories[category_id].split(
            )[:-1], categories[category_id].split()[-1]
            # Join to handle names consisting of multiple words
            category_name = ' '.join(category_name)
            print("Hello: " + f"{transaction}")
            # Count based on category type
            if category_name not in total_cost:
                total_cost[category_name] = float(transaction["amount"])
            else:
                total_cost[category_name] += float(transaction["amount"])

            if category_type == 'income':
                income[category_name] = income.get(category_name, 0) + 1
            elif category_type == 'expense':
                expense[category_name] = expense.get(category_name, 0) + 1

    print("total cost")
    print(total_cost)
    # Calculate percentages
    total_income = sum(income.values())
    total_expense = sum(expense.values())

    income_percent = {name: f"""{count} - {count /
                                           total_income:.2%}""" for name, count in income.items()}
    expense_percent = {name: f"""{count} - {count /
                                            total_expense:.2%}""" for name, count in expense.items()}

    # Prepare the summary dictionary
    summary = {
        'total_income_transactions': total_income,
        'total_expense_transactions': total_expense,
        'total_cost_category': total_cost,
    }

    return income_percent, expense_percent, summary

# Get overall transaction analysis


def getBudget_and_goal(user_id):
    with session_scope() as session:
        today = datetime.today()

        goals = session.query(SavingGoal).filter(
            SavingGoal.user_id == user_id
        ).all()

        budget = session.query(Budget).filter(
            Budget.user_id == user_id
        ).all()

        goal_result = [{
            'target_amount': t.target_amount,
            'target_date': t.target_date,
            'target': t.target,
            'created_at': t.created_at
        } for t in goals]

        budget_result = [{
            'budget_amount': t.budget_amount,
        } for t in budget]

        return goal_result, budget_result


def getOverAllTransactionAnalyze(user_id):
    with session_scope() as session:

        today = datetime.today()
        # first_day_of_month = datetime(today.year, today.month, 1)
        # next_month = today.month + 1 if today.month < 12 else 1
        # next_year = today.year if today.month < 12 else today.year + 1
        # last_day_of_month = datetime(next_year, next_month, 1)

        first_day_of_year = datetime(today.year, 1, 1)
        print(first_day_of_year)
        last_day_of_year = datetime(today.year + 1, 1, 1)
        print(last_day_of_year)

        transactions = session.query(Transaction).filter(
            Transaction.user_id == user_id,
        ).all()
        # print("transaction result: ")
        # print(transactions)
        # Convert the results into a list of serializable dictionaries
        transaction_result = [{
            'transaction_id': t.transaction_id,
            'category_id': t.category_id,
            'amount': t.amount
        } for t in transactions]

        # print(transaction_result)
        # Assume categories is defined somewhere in your app
        income_percent, expense_percent, summary = categorize_transactions(
            transaction_result, categories)

        # Structure the final JSON response
        response_data = {
            'income': income_percent,
            'expense': expense_percent,
            'summary': summary
        }

        return response_data


# Create User

def createUserInDB(email, password, uid, username):
    with session_scope() as session:
        passwordhash = generate_hash(password)
        new_user = User(auth_uid=uid, email=email,
                        password_hash=passwordhash, username=username)
        session.add(new_user)
        session.commit()
        user_data = {
            "user_id": new_user.user_id,
            "email": new_user.email,
            "username": new_user.username
        }

        print(f'User {email} created successfully!')
        return user_data

        print(f'User {email} created successfully!')


def updateUserInDB(userData):

    with session_scope() as session:
        # Retrieve the user by user_id
        user = session.query(User).filter(
            User.user_id == userData['userId']).one_or_none()

        if user is None:
            print("User not found")
            return False

        # Update the user fields
        user.gender = userData.get('gender', user.gender)
        user.birth_date = datetime.strptime(
            userData['birth_date'], '%Y-%m-%d').date()
        user.address = userData.get('address', user.address)
        user.occupation = userData.get('occupation', user.occupation)
        user.income_source = ','.join(userData.get(
            'income_source', user.income_source))

        # Update the saving goals if provided in userData
        if 'goal' in userData:
            # Check if a SavingGoal exists, if not, create a new one
            if not user.saving_goals:
                new_goal = SavingGoal(
                    user_id=user.user_id,
                    target=userData['goal']
                )
                session.add(new_goal)
            else:
                for goal in user.saving_goals:
                    goal.target = userData['goal']

        # Commit the transaction
        session.commit()
        return True


def assembaleData(monthDataDict, yearDataDict):
    # monthDataDict={"total_month_income:":8,"total_month_income":5300,"total_month_expense:":8,"total_month_expense_amount":5300}
    # yearDataDict = {"total_year_income:": 8, "total_year_income_amount": 5300, "total_year_expense:": 8,
    #                  "total_year_expense_amount": 5300}
    expense_data = {
        "monthly": {
            "countData": {
                "today": "Total 8 expenses",
                "title": "$53,00",
                "persent": "+30%",
                "color": "#ed4242",
            },
            "average": "$5000",
            "sortedData": [],
        },
        "yearly": {
            "countData": {
                "today": "Total 8 expenses",
                "title": "$600,000",
                "persent": "+20%",
                "color": "#ed4242",
            },

            "average": "$5000",
            "sortedData": [],
        }
    }
    income_data = {
        "monthly": {
            "countData": {
                "today": "Total 8 expenses",
                "title": "$53,00",
                "persent": "+30%",
                "color": "#ed4242",
            },
            "average": "$5000",

        },
        "yearly": {
            "countData": {
                "today": "Total 8 expenses",
                "title": "$600,000",
                "persent": "+20%",
                "color": "#ed4242",
            },
            "average": "$5000",



        }
    }


def get_user_info(uid):
    with session_scope() as session:
        user = session.query(User).filter(User.user_id == uid).first()
        if user:
            # Extract necessary data
            user_data = {
                'id': user.user_id,
                'username': user.username,
                'created_at': user.created_at,
                'birth_date': user.birth_date,
                'occupation': user.occupation,
                'income_source': user.income_source,
                'gender': user.gender
            }
            return user_data
        return None


def get_user_id_by_uid(uid):
    with session_scope() as session:
        user = session.query(User).filter_by(auth_uid=uid).first()
        if user:
            # 提取必要的数据
            user_data = {
                'id': user.user_id,
                'username': user.username,
                'created_at': user.created_at,
                'birth_date': user.birth_date,
                'occupation': user.occupation,
                'income_source': user.income_source,
                'gender': user.gender
            }
            return user_data
        return None


def validate_date(user, year, month=None):
    registration_year = user.created_at.year
    current_year = datetime.now().year
    current_month = datetime.now().month

    print(registration_year, current_year, year)
    if year < registration_year or year > current_year:
        return None

    if year == registration_year and month:
        registration_month = user.created_at.month
        if month < registration_month or month > current_month:
            return None

    return True


def get_transactions(user_id, year, month=None):
    with session_scope() as session:
        query = session.query(Transaction).filter(
            Transaction.user_id == user_id,
            Transaction.is_shown != 1,
            func.date_format(Transaction.transaction_date, '%Y') == str(year)
        )
        if month:
            query = query.filter(func.strftime(
                '%m', Transaction.transaction_date) == str(month).zfill(2))

        return query.all()


def top_categories(transactions_by_category):
    sorted_transactions = sorted(
        transactions_by_category.items(), key=lambda x: x[1]["amount"], reverse=True)
    return sorted_transactions[:3]


def get_user_data(uid, year=None, month=None):
    user_id = get_user_id_by_uid(uid)
    if not user_id:
        return None
    with session_scope() as session:
        user = session.query(User).get(user_id)
        if not validate_date(user, year, month):
            return None

        transactions = get_transactions(user_id, year, month)
        if not transactions:
            return None

    income_data_year, expense_data_year = categorize_transactions(
        get_transactions(user_id, year))
    income_data_month, expense_data_month = categorize_transactions(
        get_transactions(user_id, year, month))

    top_income_year = top_categories(income_data_year)
    top_expense_year = top_categories(expense_data_year)
    top_income_month = top_categories(income_data_month)
    top_expense_month = top_categories(expense_data_month)

    data = {
        "year": {
            "income": [{"type": k, "value": v["amount"]} for k, v in income_data_year.items()],
            "expense": [{"type": k, "value": v["amount"]} for k, v in expense_data_year.items()],
            "top_income": [{"category": k, "transactions": v["transactions"], "amount": v["amount"]} for k, v in
                           top_income_year],
            "top_expense": [{"category": k, "transactions": v["transactions"], "amount": v["amount"]} for k, v in
                            top_expense_year]
        },
        "month": {
            "income": [{"type": k, "value": v["amount"]} for k, v in income_data_month.items()],
            "expense": [{"type": k, "value": v["amount"]} for k, v in expense_data_month.items()],
            "top_income": [{"category": k, "transactions": v["transactions"], "amount": v["amount"]} for k, v in
                           top_income_month],
            "top_expense": [{"category": k, "transactions": v["transactions"], "amount": v["amount"]} for k, v in
                            top_expense_month]
        }
    }

    return data


def getCalanderDatabyDate(user, date):
    with session_scope() as session:

        registered_at = datetime.strptime(user.get("created_at"), '%Y-%m-%d')
        query_date = datetime.strptime(date, '%Y-%m-%d')

        if query_date < registered_at:
            return {}

        transactions = session.query(Transaction).filter(
            Transaction.transaction_date == query_date.strftime(
                '%Y-%m-%d'),
            Transaction.user_id == user.get("user_id"),
            Transaction.is_shown != 1
        ).all()

        expense = 0
        income = 0
        financeData = []
        key = 0

        for transaction in transactions:
            category_name = categories.get(
                transaction.category_id, "Unknown").rsplit(' ', 1)[0]
            amount = transaction.amount
            if "expense" in categories.get(transaction.category_id, "Unknown").lower():
                stramount = "-" + str(amount)
                expense += amount
            else:
                stramount = str(amount)
                income += amount
            key += 1
            financeData.append({
                "key": key,
                "category": category_name,
                "amount": stramount,
                "transaction_id": transaction.transaction_id,
                "category_id": transaction.category_id
            })

        result = {
            "expense": expense,
            "income": income,
            "financeData": financeData
        }

        return result


def getCalanderDatabyMonth(user, month):
    with session_scope() as session:

        transactions = session.query(Transaction).filter(
            extract('year', Transaction.transaction_date) == int(month[:4]),
            extract('month', Transaction.transaction_date) == int(month[5:7]),
            Transaction.user_id == user.get("user_id"),
            Transaction.is_shown != 1
        ).all()

        expense = 0
        income = 0
        financeData = []
        key = 0

        for transaction in transactions:
            category_name = categories.get(
                transaction.category_id, "Unknown").rsplit(' ', 1)[0]
            amount = transaction.amount
            if "expense" in categories.get(transaction.category_id, "Unknown").lower():
                amount = -amount
                expense += amount
            else:
                income += amount
            key += 1
            financeData.append({
                "key": key,
                "category": category_name,
                "amount": amount,
                "transaction_id": transaction.transaction_id,
                "category_id": transaction.category_id
            })

        result = {
            "expense": expense,
            "income": income,
            "financeData": financeData
        }

        return result


def delete_transaction(transaction_id):
    with session_scope() as session:

        transaction = session.query(Transaction).filter(
            Transaction.transaction_id == transaction_id).first()
        if transaction:
            transaction.is_shown = 1
            session.commit()
            return {'status': "success"}
        else:
            return {'status': "fail"}


def edit_transaction(transaction_id, category_id, amount):
    with session_scope() as session:

        transaction = session.query(Transaction).filter(
            Transaction.transaction_id == transaction_id).first()
        if transaction:
            transaction.category_id = category_id
            transaction.amount = amount
            session.commit()
            return {'status': "success"}
        else:
            return {'status': "fail"}


def getTransactionsByUser(user):
    with session_scope() as session:
        currentUser = user.get("user")
        print(currentUser)
        date_str = currentUser.get("created_at")
        parsed_date = datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %Z')
        registered_at = parsed_date.strftime('%Y-%m-%d')
        user_id = currentUser.get("id")

        transactions = session.query(Transaction).filter(
            # Transaction.transaction_date >= registered_at,
            Transaction.user_id == user_id,
            Transaction.is_shown != 1
        ).all()

        # Initialize result dictionaries
        result_by_date = defaultdict(
            lambda: {"expense": 0, "income": 0, "financeData": []})
        result_by_month = defaultdict(
            lambda: {"expense": 0, "income": 0, "financeData": []})

        key_counter = 0

        for transaction in transactions:
            transaction_date = transaction.transaction_date.strftime(
                '%Y-%m-%d')
            transaction_month = transaction.transaction_date.strftime('%Y-%m')
            category_name = categories.get(
                transaction.category_id, "Unknown").rsplit(' ', 1)[0]
            amount = transaction.amount
            if "expense" in categories.get(transaction.category_id, "Unknown").lower():
                stramount = "-" + str(amount)
                result_by_date[transaction_date]["expense"] += amount
                result_by_month[transaction_month]["expense"] += amount
            else:
                stramount = str(amount)
                result_by_date[transaction_date]["income"] += amount
                result_by_month[transaction_month]["income"] += amount

            key_counter += 1
            transaction_data = {
                "key": key_counter,
                "category": category_name,
                "amount": stramount,
                "transaction_id": transaction.transaction_id,
                "category_id": transaction.category_id
            }
            result_by_date[transaction_date]["financeData"].append(
                transaction_data)
            result_by_month[transaction_month]["financeData"].append(
                transaction_data)

        return {
            "by_date": dict(result_by_date),
            "by_month": dict(result_by_month)
        }


def get_expense_income_data(user):
    categories = {
        1: "Salary income",
        2: "Bonus income",
        3: "Investment Income income",
        4: "Other Income income",
        5: "Business income",
        6: "Part-time Job income",
        7: "Buying and Selling income",
        8: "Housing expense",
        9: "Food expense",
        10: "Transportation expense",
        11: "Entertainment expense",
        12: "Utilities expense",
        13: "Health expense",
        14: "Insurance expense",
        15: "Education expense",
        16: "Other Expenses expense",
        17: "Investment Expens expense",
        18: "Shopping expense",
        19: "Grocery expense"
    }
    with session_scope() as session:
        currentUser = user.get("user")
        print(currentUser)
        date_str = currentUser.get("created_at")
        parsed_date = datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %Z')
        registered_at = parsed_date.strftime('%Y-%m-%d')
        user_id = currentUser.get("id")
        # user_id=user.get("id")
        # registered_at =user.get("created_at")
        transactions = session.query(Transaction).filter(
            # Transaction.transaction_date >= registered_at,
            Transaction.user_id == user_id,
            Transaction.is_shown != 1
        ).all()
        expense_data = {
            'monthly': {},
            'yearly': {
                'countData': {'today': '', 'title': '$0', 'persent': '+25%', 'color': '#ed4242'},
                'chartTitle': 'Expense Yearly Trend',
                'categoriesTitle': 'Expense Yearly Categories',
                'average': '$0',
                'sortedData': [],
                'expenseDonutChart': [],
                'expenseLineChartSeries': [{'name': 'Monthly Expense', 'data': [0] * 12}],
                'expenseLineChartCategory': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
                                             'Nov', 'Dec'],
                'expenseBarChartSeries': [{'name': 'Monthly Expense', 'data': [0] * 12}],
                'expenseBarChartCategory': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov',
                                            'Dec']
            }
        }

        income_data = {
            'monthly': {},
            'yearly': {
                'countData': {'today': '', 'title': '$0', 'persent': '+25%', 'color': '#28a745'},
                'chartTitle': 'Income Yearly Trend',
                'categoriesTitle': 'Income Yearly Categories',
                'average': '$0',
                'sortedData': [],
                'incomeDonutChart': [],
                'incomeLineChartSeries': [{'name': 'Monthly Income', 'data': [0] * 12}],
                'incomeLineChartCategory': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov',
                                            'Dec'],
                'incomeBarChartSeries': [{'name': 'Monthly Income', 'data': [0] * 12}],
                'incomeBarChartCategory': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov',
                                           'Dec']
            }
        }

        monthly_expenses = defaultdict(lambda: defaultdict(Decimal))
        yearly_expenses = defaultdict(Decimal)
        monthly_incomes = defaultdict(lambda: defaultdict(Decimal))
        yearly_incomes = defaultdict(Decimal)

        daily_expense_details = defaultdict(lambda: defaultdict(Decimal))
        daily_income_details = defaultdict(lambda: defaultdict(Decimal))

        for transaction in transactions:
            amount = transaction.amount
            date = transaction.transaction_date
            day = date.day
            month = date.strftime('%b')
            year = date.year
            category_id = transaction.category_id
            category_name = categories[category_id]

            if "income" in category_name:
                monthly_incomes[month][category_name] += amount
                yearly_incomes[category_name] += amount
                daily_income_details[month][day] += amount
            else:
                monthly_expenses[month][category_name] += amount
                yearly_expenses[category_name] += amount
                daily_expense_details[month][day] += amount

        # Process monthly data
        for month, categories in monthly_expenses.items():
            sorted_data = [{'category': k, 'transactions': 1,
                            'amount': float(v)} for k, v in categories.items()]
            expense_data['monthly'][month] = {
                'countData': {
                    'today': f"Total {len(daily_expense_details[month])} expenses",
                    'title': f"${sum(categories.values()):.2f}",
                    'persent': '+10%',  # Example percentage
                    'color': '#ed4242',
                },
                'chartTitle': 'Expense Monthly Trend',
                'categoriesTitle': 'Expense Monthly Categories',
                'average': f"${sum(categories.values()) / len(daily_expense_details[month]):.2f}",
                'sortedData': sorted_data,
                'expenseDonutChart': [{'type': k, 'value': float(v)} for k, v in categories.items()],
                'expenseLineChartSeries': [{'name': 'Daily Expense',
                                            'data': [float(daily_expense_details[month][day]) for day in
                                                     sorted(daily_expense_details[month].keys())]}],
                'expenseLineChartCategory': [str(day) for day in sorted(daily_expense_details[month].keys())],
                'expenseBarChartSeries': [{'name': 'Daily Expense',
                                           'data': [float(daily_expense_details[month][day]) for day in
                                                    sorted(daily_expense_details[month].keys())]}],
                'expenseBarChartCategory': [str(day) for day in sorted(daily_expense_details[month].keys())]
            }

        for month, categories in monthly_incomes.items():
            sorted_data = [{'category': k, 'transactions': 1,
                            'amount': float(v)} for k, v in categories.items()]
            income_data['monthly'][month] = {
                'countData': {
                    'today': f"Total {len(daily_income_details[month])} incomes",
                    'title': f"${sum(categories.values()):.2f}",
                    'persent': '+10%',  # Example percentage
                    'color': '#28a745',
                },
                'chartTitle': 'Income Monthly Trend',
                'categoriesTitle': 'Income Monthly Categories',
                'average': f"${sum(categories.values()) / len(daily_income_details[month]):.2f}",
                'sortedData': sorted_data,
                'incomeDonutChart': [{'type': k, 'value': float(v)} for k, v in categories.items()],
                'incomeLineChartSeries': [{'name': 'Daily Income',
                                           'data': [float(daily_income_details[month][day]) for day in
                                                    sorted(daily_income_details[month].keys())]}],
                'incomeLineChartCategory': [str(day) for day in sorted(daily_income_details[month].keys())],
                'incomeBarChartSeries': [{'name': 'Daily Income',
                                          'data': [float(daily_income_details[month][day]) for day in
                                                   sorted(daily_income_details[month].keys())]}],
                'incomeBarChartCategory': [str(day) for day in sorted(daily_income_details[month].keys())]
            }

        # Process yearly data
        income_data['yearly']['countData'][
            'today'] = f"Total {sum(len(v) for v in daily_income_details.values())} incomes"
        income_data['yearly']['title'] = f"${sum(yearly_incomes.values()):.2f}"
        income_data['yearly']['average'] = f"${sum(yearly_incomes.values()) / 12:.2f}"
        income_data['yearly']['sortedData'] = [{'category': k, 'transactions': 1, 'amount': float(v)} for k, v in
                                               yearly_incomes.items()]
        income_data['yearly']['incomeDonutChart'] = [
            {'type': k, 'value': float(v)} for k, v in yearly_incomes.items()]
        income_data['yearly']['incomeLineChartSeries'][0]['data'] = [
            sum(daily_income_details[month].values()) if month in daily_income_details else 0 for month in
            income_data['yearly']['incomeLineChartCategory']]
        income_data['yearly']['incomeBarChartSeries'][0]['data'] = [
            sum(daily_income_details[month].values()) if month in daily_income_details else 0 for month in
            income_data['yearly']['incomeBarChartCategory']]

        expense_data['yearly']['countData'][
            'today'] = f"Total {sum(len(v) for v in daily_expense_details.values())} expenses"
        expense_data['yearly']['title'] = f"${sum(yearly_expenses.values()):.2f}"
        expense_data['yearly']['average'] = f"${sum(yearly_expenses.values()) / 12:.2f}"
        expense_data['yearly']['sortedData'] = [{'category': k, 'transactions': 1, 'amount': float(v)} for k, v in
                                                yearly_expenses.items()]
        expense_data['yearly']['expenseDonutChart'] = [{'type': k, 'value': float(v)} for k, v in
                                                       yearly_expenses.items()]
        expense_data['yearly']['expenseLineChartSeries'][0]['data'] = [
            sum(daily_expense_details[month].values()) if month in daily_expense_details else 0 for month in
            expense_data['yearly']['expenseLineChartCategory']]
        expense_data['yearly']['expenseBarChartSeries'][0]['data'] = [
            sum(daily_expense_details[month].values()) if month in daily_expense_details else 0 for month in
            expense_data['yearly']['expenseBarChartCategory']]

        return expense_data, income_data


def setBudget(user, budgetAmount):
    try:
        with session_scope() as session:
            currentUser = user.get("user")
            print(currentUser)

            user_id = currentUser.get("id")

            budget_record = session.query(Budget).filter(
                Budget.user_id == user_id).first()

            if budget_record:
                # 如果已有记录，则更新
                budget_record.budget_amount = budgetAmount
                print(
                    f"Updated budget for user_id {user_id} with new amount {budgetAmount}.")
            else:
                # 如果没有记录，则添加新记录
                budget_record = Budget(
                    user_id=user_id, budget_amount=budgetAmount)
                session.add(budget_record)
                print(
                    f"Added new budget for user_id {user_id} with amount {budgetAmount}.")
            session.commit()

            return {'status': "success"}
    except:
        return {'status': "fail"}
