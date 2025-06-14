using System.Collections.Generic;

namespace UML
{
    public class КонтрольДоступа
    {
        private Dictionary<Группа, List<Право>> праваГрупп;

        public Группа Группа
        {
            get => default;
            set
            {
            }
        }

        public Право Право
        {
            get => default;
            set
            {
            }
        }

        public void НазначитьПраво(Группа группа, Право право)
        {
            throw new System.NotImplementedException();
        }

        public bool ПроверитьДоступ(Пользователь пользователь, Право право)
        {
            throw new System.NotImplementedException();
        }

        public void УдалитьПраво(Группа группа, Право право)
        {
            throw new System.NotImplementedException();
        }
    }
}
