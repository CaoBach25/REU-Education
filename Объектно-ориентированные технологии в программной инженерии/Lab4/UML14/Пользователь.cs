using UML14;

namespace UML
{
    public class Пользователь
    {
        public int ИдентификаторПользователя;
        public string ИмяПользователя;
        private string пароль;
        public string ЭлектроннаяПочта;

        public Группа Группа { get; set; }

        public Группа Группа1
        {
            get => default;
            set
            {
            }
        }

        public bool Войти(string пароль)
        {
            throw new System.NotImplementedException();
        }

        public void Выйти()
        {
            throw new System.NotImplementedException();
        }

        public void СменитьПароль(string новыйПароль)
        {
            throw new System.NotImplementedException();
        }
    }
}
