
__project__ = "zeusx017"
__VERSION__ = "beta"
__author__ = "Mosa Salman"
__IG_LINK__ = "instagram.com/laser01/"
__BANNER__ = ("""\033[32m
		Author {author}
		Project {project} {Version}
\033[0m""".format(
	author=__author__, project=__project__, Version=__VERSION__
	)
)

#Tools ,the command to run tool (envirments)
__metasploit__ = 'msfconsole'

#conf
conf = {'banner':__BANNER__,
		'version':__VERSION__,
		'instagram':__IG_LINK__,
		'project':__project__,
		'author':__author__,
		'msfconsole':__metasploit__
		}

def getConf():
	return conf
