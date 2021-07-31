import React, { Component } from "react";
import axios from "axios";

const todoItems = [{}];
class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      viewCompleted: false,
      manhwaList: todoItems,
    };
  }
  componentDidMount() {
    this.refreshList();
  }

  refreshList = () => {
    axios
      .get("/api/manhwa")
      .then((res) => this.setState({ manhwaList: res.data }));
  };

  renderItems = () => {
    const itemslist = this.state.manhwaList;
    return itemslist.map((item) => (
      <div>
        <div className="row justify-content-center">
          <div className="col-md-6 col-md-offset-3 d-flex flex-row">
            <div className="p-1">
              <img src={item.cover_image} alt={item.description} />
            </div>
            <div>
              <div className="d-flex flex-column p-1">
                <h3>{item.title} </h3>
                <p>{item.description} </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    ));
  }

  render() {
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
              <p>
                I remember reading Solo leveling get hooked and trying to
                find good Manhwas - the struggle is real 😰.
              </p>
              <p> Here is a gift from me to the community</p>
            </div>
          </div>
        </div>
        {this.renderItems()}
        <div className="row justify-content-center">
            <div className="col-md-6 col-md-offset-3">
            </div>
        </div>
      </main>
    );
  }
}

export default Home;
