const html = await (await fetch('/config.html')).text()
console.log(html)
function Home() {
  return <div dangerouslySetInnerHTML={{ __html: html }} />
}

export default Home;
