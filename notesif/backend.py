from django_cas.backends import CASBackend
import ldap

class PopulatedCASBackend(CASBackend):	
    """CAS authentication backend with user data populated from AD"""

    def authenticate(self, ticket, service):
        """Authenticates CAS ticket and retrieves user data"""

        user = super(PopulatedCASBackend, self).authenticate(
        ticket, service)

        print user.username

        l = ldap.initialize("ldap://auth.insa-lyon.fr")
        u = l.search_s('dc=insa-lyon,dc=fr', ldap.SCOPE_SUBTREE, "uid="+user.username, attrlist=["givenname", "sn", "displayname", "mail", "telephonenumber","supannentiteaffectation","roomnumber","street","employeetype","uidnumber", "gidnumber","employeenumber","businesscategory","uid","departmentnumber", "supannEtuId"])
        
        if not u:
            print "User is not in LDAP..."
        else:
            print "User is in LDAP"

        if u[0][1]['employeeType'] == ['student']:
            print "User is a Student"
        else:
            print "User is not a Student"
            
        print u

        return user
