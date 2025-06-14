from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# 1. Создание Байесовской сети
risk_model = BayesianNetwork([
    ('Технические Риски', 'Финансовые Риски'),
    ('Рыночные Риски', 'Финансовые Риски'),
    ('Регуляторные Риски', 'Финансовые Риски')
])

# 2. Определение таблиц условных вероятностей (CPDs)
cpd_tech = TabularCPD(
    variable='Технические Риски',
    variable_card=2,
    values=[[0.7], [0.3]]  # 70% отсутствия, 30% наличия
)

cpd_market = TabularCPD(
    variable='Рыночные Риски',
    variable_card=2,
    values=[[0.6], [0.4]]  # 60% отсутствия, 40% наличия
)

cpd_regulatory = TabularCPD(
    variable='Регуляторные Риски',
    variable_card=2,
    values=[[0.8], [0.2]]  # 80% отсутствия, 20% наличия
)

cpd_financial = TabularCPD(
    variable='Финансовые Риски',
    variable_card=2,
    values=[
        [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2],  # Отсутствие финансовых рисков
        [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]   # Наличие финансовых рисков
    ],
    evidence=['Технические Риски', 'Рыночные Риски', 'Регуляторные Риски'],
    evidence_card=[2, 2, 2]
)

# 3. Добавление CPD в модель
risk_model.add_cpds(cpd_tech, cpd_market, cpd_regulatory, cpd_financial)

# Проверка модели
if risk_model.check_model():
    print("Модель корректна.")

# 4. Вывод вероятностей рисков
inference = VariableElimination(risk_model)

# Расчёт вероятности финансовых рисков
result = inference.query(variables=['Финансовые Риски'])
print(result)

# Расчёт условной вероятности
conditional_result = inference.query(variables=['Финансовые Риски'], evidence={'Технические Риски': 1})
print(conditional_result)