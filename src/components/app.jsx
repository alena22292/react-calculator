import React, { Component } from 'react';
import Buttons from './buttons';

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      current: '0',
      previous: [],
      next: false
    };
  }

  reset = () => {
    this.setState({ current: '0' });
  }

  addToCurrent = (val) => {
    console.log(val);
    if (["/", "-", "+", "*"].indexOf(val) > -1) {
      const { previous } = this.state;
      previous.push(this.state.current + val);
      this.setState({ previous, next: true });
    } else {
      if ((this.state.current === "0" && val !== ".") || this.state.next) {
        this.setState({ current: val, next: false });
      } else {
        this.setState({ current: this.state.current + val });
      }
    }
  }

  calculate = (val) => {
    let { previous, current, next} = this.state;
    if (previous.length > 0) {
      current = eval(String(previous[previous.length - 1] + current));
      this.setState({ current, previous, next: true });
    }
  }

  render() {
    const buttons = [
      { symbol: 'C', cols: 3, action: this.reset },
      { symbol: '/', cols: 1, action: this.addToCurrent },
      { symbol: '7', cols: 1, action: this.addToCurrent },
      { symbol: '8', cols: 1, action: this.addToCurrent },
      { symbol: '9', cols: 1, action: this.addToCurrent },
      { symbol: '*', cols: 1, action: this.addToCurrent },
      { symbol: '4', cols: 1, action: this.addToCurrent },
      { symbol: '5', cols: 1, action: this.addToCurrent },
      { symbol: '6', cols: 1, action: this.addToCurrent },
      { symbol: '-', cols: 1, action: this.addToCurrent },
      { symbol: '1', cols: 1, action: this.addToCurrent },
      { symbol: '2', cols: 1, action: this.addToCurrent },
      { symbol: '3', cols: 1, action: this.addToCurrent },
      { symbol: '+', cols: 1, action: this.addToCurrent },
      { symbol: '0', cols: 2, action: this.addToCurrent },
      { symbol: '.', cols: 1, action: this.addToCurrent },
      { symbol: '=', cols: 1, action: this.calculate }
    ];
    return (
      <div className="app">
        { this.state.previous.length > 0 ? <div className="floaty-last">{this.state.previous[this.state.previous.length - 1]}</div> : null }
        <h1>Calculator</h1>
        <input className="result" type="text" value={this.state.current} />
        {buttons.map((btn, i) => {
          return <Buttons key={btn.symbol} symbol={btn.symbol} cols={btn.cols} action={ symbol => btn.action(symbol) } />;
        })}
      </div>
    );
  }
}

export default App;
