These are the instructions I ran on 9th Nov 08 on Hardy and 10th Nov 08 on Etch to test the deployment chapter.

With these commands the sample application installs and works perfectly.


mkdir lib
cd lib
svn co http://authkit.org/svn/AuthKit/trunk AuthKit
cd AuthKit
/home/simplesite/env/bin/python setup.py develop
cd ../
hg clone http://pylonshq.com/hg/pylons-dev
cd pylons-dev
cat <<EOF> setup.cfg 
[egg_info]
#tag_build = dev
#tag_svn_revision = true
EOF

I also needed to change Pylons to rely on FormEncode 1.0, not 1.1 so that this didn't break.

/home/simplesite/env/bin/python setup.py develop
cd ../
svn co http://svn.sqlalchemy.org/sqlalchemy/trunk/ SQLAlchemy
cd SQLAlchemy
echo 0.5.0 > VERSION
cat <<EOF> setup.cfg 
[egg_info]
#tag_build = dev
#tag_svn_revision = true
EOF

change SQLAlchemy/lib/sqlalchemy.__version__ to 0.5 rather than svn so that the paginator worked

/home/simplesite/env/bin/python setup.py develop
cd ../
/home/simplesite/env/bin/easy_install -U "FormEncode>=1.0,<=1.0.99"
cd ../



