import React, { Component } from "react";
import axios from "axios";
import { Spinner } from "reactstrap";
import InfiniteScroll from "react-infinite-scroll-component";
import Manhwa from "./components/Manhwa";
import Modal from "./components/Modal";
import ListModal from "./components/CreateListModal";
import "./Home.css";
import "./Manhwa.css";
var x = null;
class Home extends Component {
  constructor(props) {
    super(props);
    this.addActiveManhwa = this.addActiveManhwa.bind(this);
    this.state = {
      manhwaList: [],
      next: null,
      more_exist: true,
      newManhwaModal: false,
      listModal: false,
      activeManhwa: [],
    };
  }
  componentDidMount() {
    this.refreshList();
    this.setState({
      activeManhwa:
        localStorage.getItem("activeManhwa") != null
          ? JSON.parse(localStorage.getItem("activeManhwa"))
          : [],
    });
  }

  refreshList = () => {
    var manhwaList = JSON.parse(localStorage.getItem("manhwaList"));
    if (manhwaList != null) {
      this.setState({ manhwaList });
    }
    axios.get("/api/manhwa").then((res) => {
      this.setState({ manhwaList: res.data.results, next: res.data.next });
      localStorage.setItem("manhwaList", JSON.stringify(res.data.results));
    });
  };
  fetchData = () => {
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

  manhwaModalToggle = () => {
    this.setState({ newManhwaModal: !this.state.newManhwaModal });
  };
  clearList = () => {
    localStorage.removeItem("activeManhwa");
    this.setState({
      activeManhwa: [],
    });
    window.location.reload();
  };
  listModalToggle = () => {
    this.setState({ listModal: !this.state.listModal });
  };
  handleListModalSubmit = (data) => {
    this.listModalToggle();
  };

  handleManhwaModalSubmit = (item) => {
    this.manhwaModalToggle();
    const formData = new FormData();
    for (var key in item) {
      formData.append(key, item[key]);
    }
    axios({
      method: "post",
      url: "/api/manhwa/",
      data: formData,
      headers: {
        "Accept-Language": "en-US,en;q=0.8",
        "Content-Type": `multipart/form-data`,
      },
    });
  };
  handleListModalSubmit = (item) => {
    item = { ...item, manhwas: this.state.activeManhwa };
    axios({
      method: "post",
      url: "/api/list/",
      data: JSON.stringify(item),
      headers: {
        accept: "application/json",
        "Accept-Language": "en-US,en;q=0.8",
        "Content-Type": `application/json`,
      },
    });
  };

  addActiveManhwa = (manhwa) => {
    const index = this.state.activeManhwa.indexOf(manhwa);
    var activeManhwa = this.state.activeManhwa;
    if (index > -1) {
      activeManhwa.splice(index, 1);
    } else {
      activeManhwa = [...activeManhwa, manhwa];
    }
    this.setState({ activeManhwa: activeManhwa }, () => {
      localStorage.setItem(
        "activeManhwa",
        JSON.stringify(this.state.activeManhwa)
      );
    });
  };

  render() {
    return (
      <main className="container">
        <div className="navbar d-flex justify-content-end">
          <button className="btn btn-primary mr-2" onClick={this.clearList}>
            Clear list
          </button>
          <button
            className="btn btn-primary mr-2"
            onClick={this.listModalToggle}
          >
            Generate list
          </button>
          <button
            className="btn btn-primary mr-2"
            onClick={this.manhwaModalToggle}
          >
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
                selected={this.state.activeManhwa.includes(item.slug)}
                onChange={this.addActiveManhwa}
              />
            ))}
          </div>
        </InfiniteScroll>
        {this.state.newManhwaModal ? (
          <Modal
            toggle={this.manhwaModalToggle}
            onSave={this.handleManhwaModalSubmit}
          />
        ) : null}
        {this.state.listModal ? (
          <ListModal
            toggle={this.listModalToggle}
            onSave={this.handleListModalSubmit}
            onCancel={this.listModalToggle}
          />
        ) : null}
      </main>
    );
  }
}

export default Home;
