# -*- coding: utf-8 -*-


def test_description_for_feed():
    from sphinxcontrib.feed import get_description_for_feed

    ctx = {
        'body': '''<div class=section id=sphinx-2017-07-sphinx> <h1>2017/07/11 Sphinx Night 2017.07 <a class=headerlink href="http://example.com/path/to/sphinx-night-201707/index.html#sphinx-night-2017-07-sphinx" title=Permalink for this headline>¶</a></h1> <p><em>Category: 'Sphinx'</em></p> <p><a class="reference internal" href="http://example.com/path/to/sphinx-night-201706/index.html"><span class=doc>Previous</span></a><h2>Self introduce<a class=headerlink href="http://example.com/path/to/sphinx-night-201707/index.html#id1" title=Permalink for this headline>¶</a></h2> <ul class=simple>'''
    }

    expect = '''<div class=section id=sphinx-2017-07-sphinx>  <p><em>Category: 'Sphinx'</em></p> <p><a class="reference internal" href="http://example.com/path/to/sphinx-night-201706/index.html"><span class=doc>Previous</span></a><h2>Self introduce</h2> <ul class=simple>'''

    actual = get_description_for_feed(ctx)

    assert expect == actual
