using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;

namespace UML
{
    public class User
    {
        public int UserID;
        public string UserName;
        private string password;
        public string Email;

        public Group Group
        {
            get => default;
            set
            {
            }
        }

        public bool Login(string password)
        {
            throw new System.NotImplementedException();
        }

        public void Logout()
        {
            throw new System.NotImplementedException();
        }

        public void ChangePassword(string newPassword)
        {
            throw new System.NotImplementedException();
        }
    }
}