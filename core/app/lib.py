
def list_all_pod(con):
    print("Listing pods with their IPs:")
    ret = con.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))


def list_pod_in_ns(con, ns):
    print("Listing pods with their IPs:")
    ret = con.list_namespaced_pod(watch=False, namespace=ns)
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
        read_pods_in_ns(con, ns, i.metadata.name)

def read_pods_in_ns(con, ns, pod_name):
    print("Listing pods with their IPs:")
    ret = con.read_namespaced_pod(watch=False, namespace=ns, podname=pod_name)
    for i in ret.items:
        print(i)

def list_all_namespaced_deployment(con, ns):
    ret = con.list_namespaced_deployment(namespace)
    for i in ret.items:
        read_pods_in_ns(con, ns, i)

def read_pods_in_ns(con, ns, name):
    print("Listing pods with their IPs:")
    ret = con.read_namespaced_deployment(name, namespace, pretty=pretty)
    for i in ret.items:
        print(i)

def list_all_namespaces(con):
    namespaces = []
    ret = con.list_namespace()
    for i in ret.items:
        namespaces.append(i.metadata.name)
    return namespaces

def get_node(con):
    ret = con.list_node()
    return ret

def list_namespaced_deployment(con, ns):
    ret = con.list_namespaced_deployment(ns)
    print("These are the deployments in namespace "+ ns+'\n')
    for i in ret.items:
        print(i.metadata.name) 
        read_pods_in_ns(con, ns, i.metadata.name)

def read_pods_in_ns(con, ns, name):
    ret = con.read_namespaced_deployment(name, ns, pretty='pretty')
    for i in ret.spec.template.spec.containers:
        print(i.image + "\n")