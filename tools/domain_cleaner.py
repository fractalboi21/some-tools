#rubbish to clean domain
# https://hackertarget.com/sqlmap-tutorial/ => hackertarget.com
# https://docs.python.org/3/library/typing.html => python.org
# https://help.one.com/hc/en-us/articles/ => one.com

top_level_domains = ["com","org","in","net","gov"]

# if no_of_words >= 3:
#         return domain[0].split(".")[-2] + "." + domain[0].split(".")[-1]
# else:
#     return clean_domain

def url2domain_name(url: str) -> str:
    var = url.split("//")
    domain = var[1].split("/")
    clean_domain = domain[0]
    no_of_words = len(domain[0].split("."))
    return clean_domain

lst_of_url = ["https://www.google.com/search?q=subdomain&oq=subdomain&aqs=chrome..69i57j0i67l4j69i60l3.2911j0j7&sourceid=chrome&ie=UTF-8",
      "https://www.wpbeginner.com/glossary/subdomain/#:~:text=A%20subdomain%20is%20an%20additional,store.yourwebsite.com",
      "https://docs.python.org/3/",
      "https://www.binarytides.com/sqlmap-hacking-tutorial/",
      "https://www.google.co.in/search/?q=ABC",
      "https://www.veracode.com/security/xss",
      "https://help.one.com/hc/en-us/articles/115005587509-What-is-a-top-level-domain-",
      "https://docs.python.org/3/library/typing.html",
      "https://hackertarget.com/sqlmap-tutorial/"] 
    
def domain_type_checker(url):
    if str(url).count(".") == 2 and url.split(".")[0] == "www":
        return "domain"
    else:
        return "could be sub-domain"
    