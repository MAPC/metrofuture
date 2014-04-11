require 'spec_helper'

describe CommunitySubtype do

  before { @subtype = CommunitySubtype.new(name: "Something", abbr: "smthg") }

  subject { @subtype }
  
  it { should respond_to :name }
  it { should respond_to :abbr }

  it { should respond_to :community_type }
  
  it { should be_valid }

  describe "when name is blank" do
    before { @subtype.name = " " }
    it { should_not be_valid }
  end

 describe "when name is too short" do
    before { @subtype.name = "a" * 2 }
    it { should_not be_valid }
  end 

  describe "when name is too long" do
    before { @subtype.name = "a" * 71 }
    it { should_not be_valid }
  end

end
