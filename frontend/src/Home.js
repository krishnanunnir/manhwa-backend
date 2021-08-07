import React, { Component } from "react";
import axios from "axios";
import { Spinner } from "reactstrap";
import InfiniteScroll from "react-infinite-scroll-component";
import Manhwa from "./components/Manhwa";
import Modal from "./components/Modal";
import "./Home.css";
import "./Manhwa.css";

const todoItems = [{}];
class Home extends Component {
  constructor(props) {
    super(props);
    this.addActiveManhwa = this.addActiveManhwa.bind(this);
    this.state = {
      manhwaList: todoItems,
      next: null,
      more_exist: true,
      modal: false,
      activeManhwa: [],
    };
  }
  componentDidMount() {
    this.refreshList();
  }

  refreshList = () => {
    axios
      .get("/api/manhwa")
      .then((res) =>
        this.setState({ manhwaList: res.data.results, next: res.data.next })
      );
  };
  fetchData = () => {
    console.log("Fetching data");
    axios.get(this.state.next).then((res) => {
      var has_more = false;
      if (res.data.next) {
        has_more = true;
      }
      var data = {
        next: res.data.next,
        manhwaList: this.state.manhwaList.concat(res.data.results),
        more_exist: has_more,
      };
      this.setState(data);
    });
  };

  toggle = () => {
    this.setState({ modal: !this.state.modal });
  };

  handleSubmit = (item) => {
    this.toggle();
    axios.post("/api/manhwa/", item, {
      headers: {
        accept: "application/json",
        "Accept-Language": "en-US,en;q=0.8",
        "Content-Type": `multipart/form-data; boundary=${item._boundary}`,
      },
    });
  };

  addActiveManhwa = (manhwa) => {
    const index = this.state.activeManhwa.indexOf(manhwa);
    console.log(index);
    if (index > -1) {
      this.state.activeManhwa.splice(index, 1);
    } else {
      this.setState({ activeManhwa: this.state.activeManhwa.concat(manhwa) });
    }
  };

  render() {
    return (
      <main className="container">
        <div className="navbar d-flex justify-content-end">
          <button className="btn btn-primary mr-2" onClick={this.toggle}>
            Add a new Manhwa
          </button>
        </div>

        <div className="row justify-content-center">
          <div className="col-md-6 col-md-offset-3">
            <h1>Find the best Manhwas</h1>
          </div>
        </div>
        <div className="mb-24">
          <div className="row justify-content-center">
            <div className="col-md-6 col-md-offset-3">
              <p>
                I remember reading Solo leveling get hooked and trying to find
                good Manhwas - the struggle is real 😰.
              </p>
              <p> Here is a gift from me to the community</p>
            </div>
          </div>
        </div>
        <InfiniteScroll
          dataLength={this.state.manhwaList.length} //This is important field to render the next data
          next={this.fetchData}
          hasMore={this.state.more_exist}
          loader={
            <div style={{ textAlign: "center" }}>
              <Spinner color="secondary" />
            </div>
          }
          endMessage={
            <p style={{ textAlign: "center" }}>
              <b>Yay! You have seen it all</b>
            </p>
          }
          // below props only if you need pull down functionality
        >
          <div>
            {this.state.manhwaList.map((item) => (
              <Manhwa
                key={item.id}
                item={item}
                selected={this.state.activeManhwa.includes(item)}
                onChange={this.addActiveManhwa}
              />
            ))}
          </div>
        </InfiniteScroll>
        {this.state.modal ? (
          <Modal toggle={this.toggle} onSave={this.handleSubmit} />
        ) : null}
      </main>
    );
  }
}

export default Home;
