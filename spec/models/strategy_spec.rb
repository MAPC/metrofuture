require 'spec_helper'

describe Strategy do

  before { @strategy = Strategy.new(title: "Inner Core", number: 3) }

  subject { @strategy }
  
  it { should respond_to :title }
  it { should respond_to :number }

  it { should be_valid }

  describe "when title is blank" do
    before { @strategy.title = " " }
    it { should_not be_valid }
  end

  describe "when title is too short" do
    before { @strategy.title = "a" * 2 }
    it { should_not be_valid }
  end 

  describe "when title is too long" do
    before { @strategy.title = "a" * 150 }
    it { should_not be_valid }
  end

  describe "when number is blank" do
    before { @strategy.number = " " }
    it { should_not be_valid }
  end
end
