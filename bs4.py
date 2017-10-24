# coding:utf8
from bs4 import BeautifulSoup
print BeautifulSoup

# html_doc = """
# <!doctype html>
# <html lang="zh" class=""><head><meta charset="utf-8"/><title data-react-helmet="true">使用 Headless Chrome 进行页面渲染</title><meta name="renderer" content="webkit"/><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0"/><meta name="force-rendering" content="webkit"/><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/><meta name="google-site-verification" content="FTeR0c8arOPKh8c5DYh_9uu98_zJbaWw53J-Sch9MTg"/><link rel="shortcut icon" href="https://static.zhihu.com/static/favicon.ico" type="image/x-icon"/><link href="//static.zhihu.com/hemingway/editor.2637af496793564e9a55.js" rel="stylesheet"/><link href="//static.zhihu.com/hemingway/app.868659f9522e52772dd2.js" rel="stylesheet"/><link href="//static.zhihu.com/hemingway/app.eb65f43717f79e87ba612a22fb19ff8c.css" rel="stylesheet"/><link href="//static.zhihu.com/hemingway/raven.a2b0d104748e47583f47.js" rel="stylesheet"/><link href="//static.zhihu.com/hemingway/common.5de19e2e6119a2d3832a.js" rel="stylesheet"/><style></style></head><body><div id="react-root"><div><div class="Layout av-cardBackground" data-zop-userToken="{&quot;userToken&quot;:&quot;cleartime&quot;}"><div class="Layout-navbarHolder"><header class="Navbar"><div class="Navbar-logo-wrapper"><a class="Navbar-logo icon-ic_zhihu_logo" href="//www.zhihu.com" target="_blank" rel="noopener" aria-label="知乎首页"></a></div><div class="Navbar-postTitle Navbar-title Navbar-titleMr60"><a href="https://zhuanlan.zhihu.com/wxyyxc1992"><img class="Navbar-columnIcon" alt="某熊的全栈之路" src="https://pic2.zhimg.com/v2-3c441415846977fe344039486f932e19_m.jpg"/></a><div class="Navbar-postTitleName"><span class="Navbar-postTitleMeta">首发于</span><a class="Navbar-postTitleMain" href="https://zhuanlan.zhihu.com/wxyyxc1992">某熊的全栈之路</a></div></div><div class="Navbar-functionality"><a class="Navbar-write"><i class="icon icon-ic_nav_new"></i>写文章</a><div class="Menu Navbar-menu"><button class="Button Button Button--plain MenuButton MenuButton-listen-hover icon icon-ic_nav_more" aria-label="更多选项" type="button"></button><div class="Menu-dropdown" style="visibility:hidden;"></div></div></div></header></div><div></div><div class="Layout-main av-card av-paddingBottom av-bodyFont Layout-titleImage--normal"><div class="PostIndex-header av-paddingTop av-card" data-zop="{&quot;authorName&quot;:&quot;王下邀月熊&quot;,&quot;itemId&quot;:&quot;26810049&quot;,&quot;title&quot;:&quot;使用 Headless Chrome 进行页面渲染&quot;,&quot;type&quot;:&quot;article&quot;}"><div class="TitleImage"><img alt="使用 Headless Chrome 进行页面渲染" src="https://pic4.zhimg.com/v2-d97aee26279119093785545d0e585407_r.png" class="TitleImage-imagePure"/></div><h1 class="PostIndex-title av-paddingSide av-titleFont">使用 Headless Chrome 进行页面渲染</h1><div class="PostIndex-author"><a href="https://www.zhihu.com/people/wxyyxc1992" target="_blank"><img class="Avatar-hemingway PostIndex-authorAvatar Avatar--xs" alt="王下邀月熊" src="https://pic2.zhimg.com/v2-a627d79d2ed03fe6f83a11743a18d909_xs.jpg" srcset="https://pic2.zhimg.com/v2-a627d79d2ed03fe6f83a11743a18d909_l.jpg 2x"/></a><a href="https://www.zhihu.com/people/wxyyxc1992" target="_blank" class="PostIndex-authorName">王下邀月熊</a><span class="Bull"></span><div class="HoverTitle" data-hover-title="Tue, May 9, 2017 9:24 PM"><time datetime="Tue May 09 2017 21:24:15 GMT+0800 (CST)">5 months ago</time></div></div></div><div class="RichText PostIndex-content av-paddingSide av-card"><blockquote><p><a href="https://zhuanlan.zhihu.com/p/26810049" class="internal">使用 Headless Chrome 进行页面渲染</a> 从属于笔者的<a href="http://link.zhihu.com/?target=https%3A//parg.co/bMe" class=" wrap external" target="_blank" rel="nofollow noreferrer"> Web 开发基础与工程实践<i class="icon-external"></i></a>系列文章，主要介绍了使用 Node.js 利用 Chrome Remote Protocol 远程控制 Headless Chrome 渲染界面的基础用法。本文涉及的参考与引用资料统一列举在<a href="http://link.zhihu.com/?target=https%3A//parg.co/btv" class=" wrap external" target="_blank" rel="nofollow noreferrer">这里<i class="icon-external"></i></a>。</p></blockquote><p>近日笔者在为 <a href="http://link.zhihu.com/?target=https%3A//github.com/wxyyxc1992/declarative-crawler" class=" wrap external" target="_blank" rel="nofollow noreferrer">declarative-crawler<i class="icon-external"></i></a> 编写动态页面的蜘蛛，即在<a href="https://zhuanlan.zhihu.com/p/26691496" class="internal">使用 declarative-crawler 爬取知乎美图</a> 一文中介绍的 HeadlessChromeSpider 时，需要选择某个无界面浏览器以执行 JavaScript 代码来动态生成页面。之前笔者往往是使用 PhantomJS 或者 Selenium 执行动态页面渲染，而在 Chrome 59 之后 Chrome 提供了 Headless 模式，其允许在命令行中使用 Chromium 以及 Blink 渲染引擎提供的完整的现代 Web 平台特性。需要注意的是，Headless Chrome 仍然存在一定的局限，相较于 Nightmare 或 Phantom 这样的工具， Chrome 的远程接口仍然无法提供较好的开发者体验。我们在下文介绍的代码示例中也会发现，目前我们仍需要大量的模板代码进行控制。</p><h1>安装与启动</h1><p>在 Chrome 安装完毕后我们可以利用其包体内自带的命令行工具启动：</p><div class="highlight"><pre><code class="language-text"><span></span>$ chrome --headless --remote-debugging-port=9222 https://chromium.org
# </code></pre></div><p>笔者为了部署方便，使用<a href="http://link.zhihu.com/?target=https%3A//hub.docker.com/r/justinribeiro/chrome-headless/" class=" wrap external" target="_blank" rel="nofollow noreferrer"> Docker 镜像<i class="icon-external"></i></a>来进行快速部署，如果你本地存在 Docker 环境，可以使用如下命令快速启动：</p><div class="highlight"><pre><code class="language-text"><span></span>docker run -d -p 9222:9222 justinribeiro/chrome-headless
# </code></pre></div><p>如果是在 Mac 下本地使用的话我们还可以创建命令别名：</p><div class="highlight"><pre><code class="language-text"><span></span>alias chrome="/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"
# alias chrome-canary="/Applications/Google\ Chrome\ Canary.app/Contents/MacOS/Google\ Chrome\ Canary"
# alias chromium="/Applications/Chromium.app/Contents/MacOS/Chromium"
# </code></pre></div><p>如果是在 Ubuntu 环境下我们可以使用 deb 进行安装：</p><div class="highlight"><pre><code class="language-text"><span></span># Install Google Chrome
# # https://askubuntu.com/questions/79280/how-to-install-chrome-browser-properly-via-command-line
# sudo apt-get install libxss1 libappindicator1 libindicator7
# wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# sudo dpkg -i google-chrome*.deb  # Might show "errors", fixed by next line
# sudo apt-get install -f
# </code></pre></div><p>chrome 命令行也支持丰富的命令行参数，--dump-dom 参数可以将 document.body.innerHTML 打印到标准输出中：</p><div class="highlight"><pre><code class="language-text"><span></span>chrome --headless --disable-gpu --dump-dom https://www.chromestatus.com/
# </code></pre></div><p>而 --print-to-pdf 标识则会将网页输出位 PDF：</p><div class="highlight"><pre><code class="language-text"><span></span>chrome --headless --disable-gpu --print-to-pdf https://www.chromestatus.com/
# </code></pre></div><p>初次之外，我们也可以使用 --screenshot 参数来获取页面截图：</p><div class="highlight"><pre><code class="language-text"><span></span>chrome --headless --disable-gpu --screenshot https://www.chromestatus.com/

# # Size of a standard letterhead.
# chrome --headless --disable-gpu --screenshot --window-size=1280,1696 https://www.chromestatus.com/

# # Nexus 5x
# chrome --headless --disable-gpu --screenshot --window-size=412,732 https://www.chromestatus.com/
# </code></pre></div><p>如果我们需要更复杂的截图策略，譬如进行完整页面截图则需要利用代码进行远程控制。</p><h1>代码控制</h1><h2>启动</h2><p>在上文中我们介绍了如何利用命令行来手动启动 Chrome，这里我们尝试使用 Node.js 来启动 Chrome，最简单的方式就是使用 child_process 来启动：</p><div class="highlight"><pre><code class="language-text"><span></span>const exec = require('child_process').exec;

# function launchHeadlessChrome(url, callback) {
#   // Assuming MacOSx.
#   const CHROME = '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome';
# }

# launchHeadlessChrome('https://www.chromestatus.com', (err, stdout, stderr) =&gt; {
#   ...
# });
# </code></pre></div><h2>远程控制</h2><p>这里我们使用 <a href="http://link.zhihu.com/?target=https%3A//github.com/cyrus-and/chrome-remote-interface" class=" wrap external" target="_blank" rel="nofollow noreferrer">chrome-remote-interface<i class="icon-external"></i></a> 来远程控制 Chrome ，实际上 chrome-remote-interface 是对于 <a href="http://link.zhihu.com/?target=https%3A//chromedevtools.github.io/devtools-protocol/tot/Input/" class=" wrap external" target="_blank" rel="nofollow noreferrer">Chrome DevTools Protocol<i class="icon-external"></i></a> 的远程封装，我们可以参考协议文档了解详细的功能与参数。使用 npm 安装完毕之后，我们可以用如下代码片进行简单控制：</p><div class="highlight"><pre><code class="language-text"><span></span>const CDP = require('chrome-remote-interface');

# CDP((client) =&gt; {
#     // extract domains
#     const {Network, Page} = client;
#     // setup handlers
#     Network.requestWillBeSent((params) =&gt; {
#         console.log(params.request.url);
#     });
#     Page.loadEventFired(() =&gt; {
#         client.close();
#     });
#     // enable events then start!
#     Promise.all([
#         Network.enable(),
#         Page.enable()
#     ]).then(() =&gt; {
#         return Page.navigate({url: 'https://github.com'});
#     }).catch((err) =&gt; {
#         console.error(err);
#         client.close();
#     });
# }).on('error', (err) =&gt; {
#     // cannot connect to the remote endpoint
#     console.error(err);
# });
# </code></pre></div><p>我们也可以使用 chrome-remote-interface 提供的命令行功能，譬如我们可以在命令行中访问某个界面并且记录所有的网络请求：</p><div class="highlight"><pre><code class="language-text"><span></span>$ chrome-remote-interface inspect
# &gt;&gt;&gt; Network.enable()
# { result: {} }
# &gt;&gt;&gt; Network.requestWillBeSent(params =&gt; params.request.url)
# { 'Network.requestWillBeSent': 'params =&gt; params.request.url' }
# &gt;&gt;&gt; Page.navigate({url: 'https://www.wikipedia.org'})
# { 'Network.requestWillBeSent': 'https://www.wikipedia.org/' }
# { result: { frameId: '5530.1' } }
# { 'Network.requestWillBeSent': 'https://www.wikipedia.org/portal/wikipedia.org/assets/img/Wikipedia_wordmark.png' }
# { 'Network.requestWillBeSent': 'https://www.wikipedia.org/portal/wikipedia.org/assets/img/Wikipedia-logo-v2.png' }
# { 'Network.requestWillBeSent': 'https://www.wikipedia.org/portal/wikipedia.org/assets/js/index-3b68787aa6.js' }
# { 'Network.requestWillBeSent': 'https://www.wikipedia.org/portal/wikipedia.org/assets/js/gt-ie9-c84bf66d33.js' }
# { 'Network.requestWillBeSent': 'https://www.wikipedia.org/portal/wikipedia.org/assets/img/sprite-bookshelf_icons.png?16ed124e8ca7c5ce9d463e8f99b2064427366360' }
# { 'Network.requestWillBeSent': 'https://www.wikipedia.org/portal/wikipedia.org/assets/img/sprite-project-logos.png?9afc01c5efe0a8fb6512c776955e2ad3eb48fbca' }
# </code></pre></div><p>我们也可以直接查看内置的接口文档：</p><div class="highlight"><pre><code class="language-text"><span></span>&gt;&gt;&gt; Page.navigate
# { [Function]
#   category: 'command',
#   parameters: { url: { type: 'string', description: 'URL to navigate the page to.' } },
#   returns:
#    [ { name: 'frameId',
#        '$ref': 'FrameId',
#        hidden: true,
#        description: 'Frame id that will be navigated.' } ],
#   description: 'Navigates current page to the given URL.',
#   handlers: [ 'browser', 'renderer' ] }&gt;&gt;&gt; Page.navigate
# { [Function]
#   category: 'command',
#   parameters: { url: { type: 'string', description: 'URL to navigate the page to.' } },
#   returns:
#    [ { name: 'frameId',
#        '$ref': 'FrameId',
#        hidden: true,
#        description: 'Frame id that will be navigated.' } ],
#   description: 'Navigates current page to the given URL.',
#   handlers: [ 'browser', 'renderer' ] }
# </code></pre></div><p>我们在上文中还提到需要以代码控制浏览器进行完整页面截图，这里需要利用 Emulation 模块控制页面视口缩放：</p><br><br><div class="highlight"><pre><code class="language-text"><span></span>const CDP = require('chrome-remote-interface');
# const argv = require('minimist')(process.argv.slice(2));
# const file = require('fs');

# // CLI Args
# const url = argv.url || 'https://www.google.com';
# const format = argv.format === 'jpeg' ? 'jpeg' : 'png';
# const viewportWidth = argv.viewportWidth || 1440;
# const viewportHeight = argv.viewportHeight || 900;
# const delay = argv.delay || 0;
# const userAgent = argv.userAgent;
# const fullPage = argv.full;

# // Start the Chrome Debugging Protocol
# CDP(async function(client) {
#   // Extract used DevTools domains.
#   const {DOM, Emulation, Network, Page, Runtime} = client;

#   // Enable events on domains we are interested in.
#   await Page.enable();
#   await DOM.enable();
#   await Network.enable();

#   // If user agent override was specified, pass to Network domain
#   if (userAgent) {
#   }

#   // Set up viewport resolution, etc.
#   const deviceMetrics = {
#     width: viewportWidth,
#     height: viewportHeight,
#     deviceScaleFactor: 0,
#     mobile: false,
#     fitWindow: false,
#   };
#   await Emulation.setDeviceMetricsOverride(deviceMetrics);
#   await Emulation.setVisibleSize({width: viewportWidth, height: viewportHeight});

#   // Navigate to target page

#   // Wait for page load event to take screenshot
#   Page.loadEventFired(async () =&gt; {
#     // If the `full` CLI option was passed, we need to measure the height of
#     // the rendered page and use Emulation.setVisibleSize
#     if (fullPage) {
#       const {nodeId: bodyNodeId} = await DOM.querySelector({
#         selector: 'body',
#         nodeId: documentNodeId,
#       });

#       await Emulation.setVisibleSize({width: viewportWidth, height: height});
#       // This forceViewport call ensures that content outside the viewport is
#       // rendered, otherwise it shows up as grey. Possibly a bug?
#       await Emulation.forceViewport({x: 0, y: 0, scale: 1});
#     }

#     setTimeout(async function() {
#       const buffer = new Buffer(screenshot.data, 'base64');
#       file.writeFile('output.png', buffer, 'base64', function(err) {
#         if (err) {
#           console.error(err);
#         } else {
#           console.log('Screenshot saved');
#         }
#         client.close();
#       });
#     }, delay);
#   });
# }).on('error', err =&gt; {
#   console.error('Cannot connect to browser:', err);
# });
#     transformRequest.forEach(trans =&gt; {
#       options = trans.call(ctx, options);
#     });
#     options = authHeadersTransformRequest.call(ctx, options);
#     return myHttp(url, options).then(r =&gt; {
#       let ret = r;
#       transformResponse.forEach(trans =&gt; {
#         ret = trans.call(ctx, ret, r);
#       });
#       return ret;
#     });
#   """
# soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')
# print '获取所有的链接'
# links = soup.find_all('a')
# for link in links:
# 	print link.name, link['href'], link.get_text()