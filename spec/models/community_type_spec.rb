require 'spec_helper'

describe CommunityType do

  before { @community_type = CommunityType.new(name: "Something", abbr: "smthng") }

  subject { @community_type }
  
  it { should respond_to :name }
  it { should respond_to :abbr }
  
  it { should be_valid }

  describe "when name is blank" do
    before { @community_type.name = " " }
    it { should_not be_valid }
  end

 describe "when title is too short" do
    before { @community_type.name = "a" * 2 }
    it { should_not be_valid }
  end 

  describe "when title is too long" do
    before { @community_type.name = "a" * 70 }
    it { should_not be_valid }
  end

  describe "when abbr is blank" do
    before { @community_type.abbr = " " }
    it { should_not be_valid }
  end

  describe "when abbr is too short" do
    before { @community_type.abbr = "a" }
    it { should_not be_valid }
  end

  describe "when abbr is too long" do
    before { @community_type.abbr = "a" * 70 }
    it { should_not be_valid }
  end

end
