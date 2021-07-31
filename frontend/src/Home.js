import React, { Component } from "react";

const todoItems = [{}];
class Home extends Component {
    constructor(props) {
      super(props);
      this.state = {
        viewCompleted: false,
        todoList: todoItems,
      };
    }

    render(){
        return (
            <main className="container">
                <div className="row justify-content-center">
                    <div className="col-md-6 col-md-offset-3">
                        <h1>Find the best Manhwas</h1>
                    </div>
                </div>
                <div className="mb-24">
                    <div className="row justify-content-center">
                        <div className="col-md-6 col-md-offset-3">
                        <p>I rememberrrr reading Solo leveling get hooked and trying to find good Manhwas - the struggle is real 😰.

    Here is a gift from me to the community</p>
                        </div>
                    </div>
                </div>
            <div>
            </div>
            </main>
        )
    }
}

export default Home;
