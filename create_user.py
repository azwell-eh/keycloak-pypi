from keycloak import KeycloakAdmin
from keycloak import KeycloakOpenIDConnection

keycloak_connection = KeycloakOpenIDConnection(
                        server_url="http://140.238.30.49/",
                        realm_name="master",
                        client_id="restApi",
                        client_secret_key="I8mocxy8sF6HPiOvCDLdefip0T8rUgJI",
                        verify=True)