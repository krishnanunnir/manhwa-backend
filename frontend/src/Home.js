import React, { Component } from "react";
import axios from "axios";
import Manhwa from "./components/Manhwa";
import InfiniteScroll from "react-infinite-scroll-component";

const todoItems = [{}];
class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      manhwaList: todoItems,
      next: null,
      more_exist: true,
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
            <p style={{ textAlign: "center" }}>
              <b>Loading....</b>
            </p>
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
              <Manhwa item={item} />
            ))}
          </div>
        </InfiniteScroll>
      </main>
    );
  }
}

export default Home;
