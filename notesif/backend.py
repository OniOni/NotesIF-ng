from django_cas.backends import CASBackend
import ldap

class PopulatedCASBackend(CASBackend):	
    """CAS authentication backend with user data populated from AD"""

    def authenticate(self, ticket, service):
        """Authenticates CAS ticket and retrieves user data"""

        user = super(PopulatedCASBackend, self).authenticate(
        ticket, service)

        

        l = ldap.initialize("ldap://auth.insa-lyon.fr")
        u = l.search_s('dc=insa-lyon,dc=fr', ldap.SCOPE_SUBTREE, "uid="+user.username, attrlist=["employeeType", "supannEtuId"])
        
        if not u:
            print "User is not in LDAP..."
        #else:
        #    print "User is in LDAP"

        if u[0][1]['employeeType'] != ['student']:
            print "User is not a Student"
        #else:
        #    print "User is a Student"
            
        user.get_profile().id_from_ldap = u[0][1]['supannEtuId'][0]
        user.save()
        
        print user.username + " with id " + user.id_from_ldap + " just connected."

        return user
