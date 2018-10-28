# simple scraper for everydayhealth (早安健康)
## Requirements
- requests
- lxml
## Usage
Enter a Keyword. The program automatically scrape through all the articles.    
You will receive a list of all the results in dict.    
A single dict would be in this structure : 
```
{
    title : <str>,
    date : <str>,
    author : <str>,
    body : <str>
}
```
## Demo
![image](https://github.com/chuang861012/simple-health-scraper/blob/master/demo.gif)
## Todo
A few the articles in this website are in different html structure. The program won't get the result correctly. But it won't crash. Must be fixed in the future.