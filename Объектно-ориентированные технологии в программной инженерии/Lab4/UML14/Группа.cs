using System.Collections.Generic;
using UML14;

namespace UML
{
    public class Группа
    {
        public int ИдентификаторГруппы;
        public string НазваниеГруппы;
        public string Описание;
        private List<Пользователь> пользователи;

        public Право Право { get; set; }

        public Пользователь Пользователь
        {
            get => default;
            set
            {
            }
        }

        public Право Право1
        {
            get => default;
            set
            {
            }
        }

        public void ДобавитьПользователя(Пользователь пользователь)
        {
            throw new System.NotImplementedException();
        }

        public void УдалитьПользователя(Пользователь пользователь)
        {
            throw new System.NotImplementedException();
        }

        public List<Пользователь> СписокПользователей()
        {
            throw new System.NotImplementedException();
        }
    }
}
