using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;

namespace UML
{
    public class AccessControl
    {
        private Dictionary <Group, List <Permission>> groupPermissions;

        public Group Group
        {
            get => default;
            set
            {
            }
        }

        public Permission Permission
        {
            get => default;
            set
            {
            }
        }

        public Group Group
        {
            get => default;
            set
            {
            }
        }

        public void AssignPermission(Group group, Permission permission)
        {
            throw new System.NotImplementedException();
        }

        public void RemovePermission(Group group, Permission permission)
        {
            throw new System.NotImplementedException();
        }

        public bool CheckAccess(User user, Permission permission)
        {
            throw new System.NotImplementedException();
        }
    }
}