using System;

namespace ConsoleGame
{
  class Game : SuperGame
  {
    public new static void UpdatePosition (string k, out int x, out int y){
      switch (k) {
        case "DownArrow":
        y = + 1;
        x = 0;
        break;
        case "UpArrow":
        y = - 1;
        x = 0;
        break;
        case "LeftArrow":
        x = - 1;
        y = 0;
        break;
        case "RightArrow":
        x = + 1;
        y =0;
        break;
        default: 
        x = 0;
        y = 1;
        break;
      };
    }
    public new static char UpdateCursor(string key){
      switch (key) {
        case "DownArrow":
        return 'v';
        case "UpArrow":
        return '^';
        case "LeftArrow":
        return '<';
        case "RightArrow":
        return '>';
        default: 
        return '<';
      };
    }
  public new static int KeepInBounds(int x, int maxV) {
    if (x > maxV) {
      //return maxV;
      return 0;
    } else if (x < 0) {
      //return 0;
      return maxV;
    } else {
      return x;}
    }
  public new static bool DidScore(int keyx, int keyy, int fruitx, int fruity) {
    return keyx == fruitx && keyy == fruity;
    
  }
  }
}