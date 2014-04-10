require 'spec_helper'

describe SubStrategy do

  before { @substrategy = SubStrategy.new(title: "TOD", letter: "T") }

  subject { @substrategy }
  
  it { should respond_to :title }
  it { should respond_to :letter }

  it { should be_valid }

  describe "when title is blank" do
    before { @substrategy.title = " " }
    it { should_not be_valid }
  end

 describe "when title is too short" do
    before { @substrategy.title = "a" * 2 }
    it { should_not be_valid }
  end 

  describe "when title is too long" do
    before { @substrategy.title = "a" * 170 }
    it { should_not be_valid }
  end

  describe "when letter is blank" do
    before { @substrategy.letter = " " }
    it { should_not be_valid }
  end

  describe "when letter is too long" do
    before { @substrategy.letter = "a" * 2 }
    it { should_not be_valid }
  end
end
